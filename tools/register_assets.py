#!/usr/bin/env python3
"""Register validated PNG assets from assets/inbox without external dependencies."""
import json
import re
import struct
import sys
import zlib
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "assets" / "inbox"
REGISTRY = ROOT / "assets" / "registry.json"
MAX_BYTES = 16 * 1024 * 1024
MAX_DIMENSION = 4096

def png_info(path):
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise ValueError("PNG exceeds 16 MiB limit")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    pos, header, ended = 8, None, False
    while pos + 12 <= len(data):
        length = struct.unpack(">I", data[pos:pos+4])[0]
        kind = data[pos+4:pos+8]
        end = pos + 12 + length
        if end > len(data):
            raise ValueError("truncated PNG chunk")
        payload = data[pos+8:pos+8+length]
        expected = struct.unpack(">I", data[pos+8+length:end])[0]
        actual = zlib.crc32(kind + payload) & 0xffffffff
        if expected != actual:
            raise ValueError("PNG CRC mismatch")
        if header is None:
            if kind != b"IHDR" or length != 13:
                raise ValueError("missing PNG IHDR")
            w, h, depth, color, comp, filt, interlace = struct.unpack(">IIBBBBB", payload)
            if not (1 <= w <= MAX_DIMENSION and 1 <= h <= MAX_DIMENSION):
                raise ValueError("invalid image dimensions")
            if depth != 8 or color != 6 or comp != 0 or filt != 0 or interlace not in (0,1):
                raise ValueError("requires 8-bit RGBA PNG")
            header = (w, h)
        if kind == b"IEND":
            ended = True
            if end != len(data):
                raise ValueError("unexpected trailing bytes after PNG")
            break
        pos = end
    if not ended:
        raise ValueError("missing PNG IEND")
    return header

def main():
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    entries = registry.get("assets")
    if not isinstance(entries, list):
        raise ValueError("registry.assets must be an array")
    existing = {a["src"]: a for a in entries if isinstance(a, dict) and "src" in a}
    changed = 0
    errors = []
    for path in sorted(INBOX.rglob("*.png")) if INBOX.exists() else []:
        relative = path.relative_to(ROOT).as_posix()
        try:
            w, h = png_info(path)
            meta_path = path.with_suffix(".json")
            meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
            if not isinstance(meta, dict):
                raise ValueError("metadata must be an object")
            stem = path.stem
            asset_id = str(meta.get("id") or stem).strip()
            if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", asset_id):
                raise ValueError("invalid asset id")
            category = str(meta.get("category") or path.parent.name if path.parent != INBOX else meta.get("category") or "misc")
            if not re.fullmatch(r"[a-z][a-z0-9_-]{0,31}", category):
                raise ValueError("invalid category")
            anchor = meta.get("anchor")
            if anchor is not None and (not isinstance(anchor, list) or len(anchor) != 2 or any(not isinstance(v, int) or isinstance(v, bool) for v in anchor)):
                raise ValueError("anchor must be two integer coordinates")
            footprint = meta.get("footprint")
            if footprint is not None and (not isinstance(footprint, list) or len(footprint) != 2 or any(not isinstance(v, int) or isinstance(v, bool) or v < 1 for v in footprint)):
                raise ValueError("footprint must be two positive integers")
            if any(a.get("id") == asset_id and a.get("src") != relative for a in entries):
                raise ValueError("asset ID conflicts with another file")
            entry = {
                "id": asset_id,
                "name": str(meta.get("name") or stem.replace("_", " ").replace("-", " ").title()),
                "category": category,
                "status": "candidate",
                "src": relative,
                "width": w,
                "height": h,
                "anchor": anchor,
                "footprint": footprint,
                "notes": str(meta.get("notes") or "Automatically registered; awaiting visual review.")
            }
            if relative in existing:
                previous = existing[relative]
                if previous.get("status") in ("approved", "ready", "rework"):
                    entry["status"] = previous["status"]
                if previous == entry:
                    continue
                entries[entries.index(previous)] = entry
            else:
                entries.append(entry)
            existing[relative] = entry
            changed += 1
            print("Registered:", relative)
        except (ValueError, KeyError, json.JSONDecodeError) as exc:
            errors.append(f"{relative}: {exc}")
    if errors:
        for error in errors:
            print("ERROR:", error, file=sys.stderr)
        return 1
    if changed:
        registry["updated"] = date.today().isoformat()
        REGISTRY.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Asset Factory: {changed} registry entries changed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

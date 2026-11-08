#!/usr/bin/env python3
"""Project Turnip Asset Factory v0.1: validate and preview sprite sheets."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="RGBA PNG sprite sheet")
    parser.add_argument("--output", default="build/asset_factory")
    parser.add_argument("--tile-size", type=int, default=32)
    parser.add_argument("--asset-id", default="A002")
    args = parser.parse_args()
    source = Path(args.input)
    if not source.is_file() or source.suffix.lower() != ".png":
        parser.error("Input must be an existing PNG")
    if args.tile_size <= 0:
        parser.error("Tile size must be positive")
    with Image.open(source) as opened:
        if opened.mode != "RGBA":
            parser.error("Expected RGBA PNG with alpha channel")
        image = opened.copy()
    width, height = image.size
    if width % args.tile_size or height % args.tile_size:
        parser.error(f"Dimensions {width}x{height} not divisible by {args.tile_size}")
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    tiles = []
    cols, rows = width // args.tile_size, height // args.tile_size
    for row in range(rows):
        for col in range(cols):
            box = (col * args.tile_size, row * args.tile_size,
                   (col + 1) * args.tile_size, (row + 1) * args.tile_size)
            tile = image.crop(box)
            name = f"{args.asset_id.lower()}_{row:02d}_{col:02d}.png"
            tile.save(out / name)
            tiles.append({"name": name, "row": row, "col": col,
                          "alpha_min": tile.getchannel("A").getextrema()[0],
                          "alpha_max": tile.getchannel("A").getextrema()[1]})
    preview = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    preview.alpha_composite(image)
    draw = ImageDraw.Draw(preview)
    for x in range(0, width + 1, args.tile_size):
        draw.line((x, 0, x, height), fill=(255, 255, 255, 140))
    for y in range(0, height + 1, args.tile_size):
        draw.line((0, y, width, y), fill=(255, 255, 255, 140))
    preview.save(out / "contact_sheet.png")
    manifest = {"asset_id": args.asset_id, "source": str(source),
                "tile_size": args.tile_size, "columns": cols, "rows": rows,
                "tiles": tiles, "status": "CANDIDATE"}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Exported {len(tiles)} tiles to {out}; status CANDIDATE")

if __name__ == "__main__":
    main()

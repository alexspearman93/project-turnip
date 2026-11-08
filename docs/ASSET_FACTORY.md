# Project Turnip — Asset Factory v0.1

## Purpose
Automate processing and QA of candidate sprite sheets without bypassing the art approval process in ART_BIBLE.md and ASSET_MANIFEST.md.

## Workflow
1. Create an RGBA PNG sheet with fixed 32x32 cells and no captions, borders, or baked checkerboards.
2. Commit it to `art_sources/` on a working branch.
3. GitHub Actions runs the processor and uploads an artifact ZIP containing each extracted tile, a gridded contact sheet, and machine-readable manifest.
4. Review output at native scale and in-game; only then move accepted files to `assets/` and update ASSET_MANIFEST.md.
5. A002 remains PLANNED until candidate files are actually produced and validated.

## Manual run
```bash
python -m pip install 'Pillow>=11,<13'
python tools/asset_factory.py --input art_sources/a002_sheet.png --asset-id A002
```

The GitHub Actions workflow also supports manual dispatch with a source path and asset ID.

## Limitations
- Fixed-cell extraction only. No automatic identification of objects in irregular artwork.
- Does not verify seamless tile edges, artistic quality, anchor points, or gameplay collision.
- Does not generate images via an AI API.
- Does not automatically deploy candidate sprites to the game.
- Full-alpha ground tiles are valid; alpha is reported, not treated as proof of quality.

## Next iteration
Add automated seam-edge checks for base ground tiles, a browser review gallery, and metadata-driven atlas packaging. Preserve the human approval gate.

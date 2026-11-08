# Asset Factory v0.3 — Automated asset registration

## What works
When a PNG is committed to `assets/inbox/` on `main`, GitHub Actions runs `tools/register_assets.py`. The script validates PNG structure, CRCs, dimensions and 8-bit RGBA format, then adds or updates the asset in `assets/registry.json`. The workflow commits the changed registry. The existing `asset-gallery.html` automatically reads it.

**No automatic AI generation, background removal, pixel-art review, sprite slicing, or gameplay integration is claimed at this stage.** The PNG must already be in GitHub. The workflow also depends on repository Actions being enabled and the workflow token having write permission.

## Usage
Place a transparent 8-bit RGBA PNG under `assets/inbox/`, for example `assets/inbox/rocks/mossy_rock_01.png`. Optionally put a sibling JSON file `assets/inbox/rocks/mossy_rock_01.json`:

```json
{
  "id": "A006_rock_01",
  "name": "Mossy Appalachian Rock 01",
  "category": "rock",
  "anchor": [16, 31],
  "footprint": [1, 1],
  "notes": "Candidate for A006; awaiting in-game review."
}
```

Commit the files to main. GitHub Actions should update `assets/registry.json`; the gallery then displays the new entry. The registry marks new assets as `candidate`, not approved.

## Validation and limits
- PNG signature, all chunk CRCs, IHDR and IEND validated.
- 8-bit RGBA PNG only, up to 4096×4096 and 16 MiB.
- Metadata must have a unique asset ID; anchor is optional integer [x,y], footprint optional positive integer [width,height].
- This is structural validation; it does not prove useful transparency or visual quality.
- Existing hand-registered assets are preserved.
- Local test: `python3 tools/register_assets.py`.

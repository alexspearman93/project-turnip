# Project Turnip — Asset Manifest
Version: 0.1 | Updated: 2026-11-06

## Purpose
Tracks every graphical asset from idea through in-game acceptance. This document and `ART_BIBLE.md` are the shared contract between the Art Studio and Game Development chats.

## Status definitions
- **PLANNED**: brief/specification only
- **CONCEPT**: visual reference, not integration-ready
- **CANDIDATE**: exported image(s), awaiting validation
- **READY**: validated files committed; awaiting in-game test
- **APPROVED**: integrated and tested in-game
- **REWORK**: rejected or requires fixes

## Asset registry
| ID | Asset | Status | Target files | Nominal footprint | Notes |
| --- | --- | --- | --- | --- | --- |
| A001 | Appalachian farmhouse | READY | `assets/buildings/farmhouse.png` | ~5×4 tile base; larger roof | First priority; correct filled roof and 2.5D depth |
| A002 | Grass/dirt/path tileset | PLANNED | `assets/terrain/ground.png` | 32×32 cells | Seamless organic variants and transitions |
| A003 | Hardwood tree | PLANNED | `assets/nature/hardwood.png` | 1 tile trunk anchor; larger canopy | Separate canopy/lower parts if needed |
| A004 | Pine tree | PLANNED | `assets/nature/pine.png` | 1 tile trunk anchor; larger canopy | Distinct silhouette |
| A005 | Farmer sprite sheet | PLANNED | `assets/characters/farmer.png` | ~32×48/frame | Four directions, idle/walk; consistent feet anchor |
| A006 | Mossy rocks | PLANNED | `assets/nature/rocks.png` | 1–2 tiles | Multiple silhouettes |
| A007 | Weeds, ferns, flowers | PLANNED | `assets/nature/undergrowth.png` | Variable | Ground decals versus cuttable objects |
| A008 | Creek/water tileset | PLANNED | `assets/terrain/water.png` | 32×32 cells | Edges, banks, possible animation |
| A009 | Raised earth/stone embankments | PLANNED | `assets/terrain/elevation.png` | 32×32 cells | Lip, face, corners, ramps/steps |

## Required per-asset metadata
For each candidate, append a section or update a separate metadata file documenting:
- ID, descriptive name, version, creator/source and usage rights
- Exact repository path(s) and image format
- Pixel dimensions and sheet grid (if applicable)
- World footprint, draw anchor (relative to sprite), and layering/z-sort behavior
- Direction and animation frame order, durations (if applicable)
- Dependencies, collision assumptions, palette/light direction
- Test results, approval date, and relevant commit

## File naming
Use lowercase `snake_case` names, PNG with alpha for sprites. Optional variants: `hardwood_summer_01.png`. Keep source references or editable masters under `art_sources/` only when permitted; runtime images live under `assets/`.

## Integration checklist
1. Confirm exported image exists at exact path.
2. Validate dimensions and true alpha (no faux transparent checkerboard).
3. Inspect at native size; check silhouette and palette against Art Bible.
4. Confirm base anchor and occupied tile(s).
5. Integrate via image loading with a visible fallback for failures.
6. Test rendering order, collision, camera edges, and iPhone layout.
7. Mark APPROVED only after successful live gameplay verification.

## Current implemented art
As of v0.3, visuals are drawn procedurally inside `index.html`. **No standalone production PNG sprites are registered as integrated.** The original concept image is a mood reference, not a sprite asset.

## First handoff: A001 Farmhouse
Produce a cohesive rustic timber farmhouse with a fully filled pitched roof, visible front wall, small porch/stoop, warm windows, chimney, subtle vines/weathering and believable down-right cast shadow. Match three-quarter top-down perspective and upper-left light. Provide transparent isolated PNG, exact dimensions and ground/base anchor. Do not bake in background grass, UI, text or scenery. Verify appearance in a 512×384 gameplay composition before integration.

## A001 — Appalachian farmhouse v0.2
- **Status:** READY; integrated into game code, awaiting live iPhone visual/collision testing.
- **Creator/source:** ChatGPT-generated artwork, refined and raster-exported for Project Turnip; generated asset intended for use in this project.
- **File:** `assets/buildings/farmhouse.png` (RGBA PNG, 256 × 224 px; single sprite, no sheet grid).
- **Logical footprint:** provisional 5 × 4 tiles (160 × 128 px), to be confirmed against gameplay collision.
- **Draw anchor:** provisional (128, 223) in sprite pixel coordinates, at bottom center; may require tuning during integration.
- **Layering:** world structure with base/footprint grounded at anchor; roof and overhang extend upward, requiring character occlusion review. Use upper-left lighting and subtle down-right shadow.
- **Animation:** none; static sprite.
- **Dependencies:** game image loader and Y-order/occlusion handling; collision must be defined independently from transparent sprite bounds.
- **Validation:** 512 × 384 scale mockup reviewed; live Canvas integration, alpha-edge inspection, mobile readability, and collision tests outstanding.
- **Approval:** not approved; awaiting Game Development integration and iPhone test.

## A001 integration log — 2026-11-06
- Integrated in `index.html` with `Image()` loading and procedural fallback; commit `de2e1b1728b10a20f90f2fb09e02bd04833cf8b5`.
- Rendered at 192 × 168 px, bottom-aligned to existing 5 × 4 tile house footprint and centered horizontally. Original file remains 256 × 224 px; rendered at 75% scale.
- Existing building collision retained; render placement, player overlap, mobile readability, and roof/ground alignment require live QA.
- Not yet APPROVED.

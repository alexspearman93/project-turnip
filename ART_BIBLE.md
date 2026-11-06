# Project Turnip — Art Bible
Version: 0.1 (provisional) | Status: working specification | Updated: 2026-11-06

## Vision
A cozy, nature-rich Appalachian homestead farming RPG. Rustic, lived-in, gently overgrown and inviting. The farm sits in a small valley, with wooded slopes, a creek, stone embankments, and a weathered farmhouse. The player gradually reclaims the land. Favor visual storytelling: moss, crooked fencing, fallen leaves, firewood, imperfect paths, wildflowers, and natural variation.

## Perspective and depth
- **2.5D three-quarter top-down**, NOT true isometric. Movement and farming remain on a square logical tile grid.
- Show the **front and roof** of buildings, plus a little side where appropriate. Roofs must be filled, structurally believable surfaces—not outlines.
- Trees have separate lower trunks and canopies where practical; draw/sort by foot or base Y coordinate so the farmer can walk behind them.
- Use cast shadows and restrained highlights to indicate height. Elevated terrain should have a visible lip/face, coherent edges, and accessible ramps/steps when gameplay supports them.
- Depth is visual first; do not imply a climbable elevation system until collision and navigation support it.

## Art style
- Cohesive **handcrafted-looking pixel art** with intentional pixel clusters and readable silhouettes, not smooth vector shapes or generic gradients.
- Target a moderately detailed 16/32-bit-inspired look. Avoid photorealism, AI painterly blur, excessively noisy textures, heavy black outlines, and sterile symmetry.
- Natural Appalachian foliage: broadleaf hardwoods, pines, understory, ferns, flowers, moss, stones, creek vegetation.
- Warm, welcoming lighting; daylight generally from **upper left**. Shadows fall subtly down/right. Keep direction consistent in all assets.
- Palette: muted forest greens, sage grass, warm soil browns, gray-blue stone, weathered timber, clay/rust roofs, cream/golden highlights. Saturated accent colors are for flowers, crops, and focal objects.
- Avoid a conspicuous alternating checkerboard on the ground; use organic patches and seamless variations.

## Game constraints (current implementation)
- Canvas internal resolution **512 × 384**; logical viewport **16 × 12** tiles; logical tile **32 × 32 px**.
- Current world is **32 × 24** tiles with a scrolling camera. These are implementation facts, not permanent art limits.
- Farmer is a small sprite anchored to a single tile. Large objects may extend **above and across** their logical occupied tile(s).
- Maintain legibility on an iPhone. Favor clear silhouettes and controlled detail at game scale.
- Sprite artwork should be raster PNG with **true alpha transparency**, no baked checkerboard, captions, UI, borders, drop-shadow backdrops, or stray pixels.
- Export at native pixel size when possible; nearest-neighbor scaling only. Do not antialias pixel edges.

## Working production dimensions (proposals, validate before locking)
- Ground: 32 × 32 px per tile; tileable with 1–3 variants and transition edges.
- Farmer: nominal 32 × 48 px including hat, with feet anchored at tile center/bottom; directions and animation frames should share consistent anchor and scale.
- Tree: ~64 × 96 px or 96 × 128 px, varying by species; trunk foot is the gameplay anchor.
- Rocks/weeds: 32–64 px wide, depending on collision footprint.
- Farmhouse: target ~192 × 192 px or larger, covering roughly 5 × 4 logical tiles at base. Roof may extend beyond base collision bounds.
These dimensions are **not approved asset sizes**; verify against a 512 × 384 game screenshot and coordinate with the game-development chat.

## Asset layering
Recommended conceptual layers:
1. Base terrain and path transitions
2. Ground decals, soil, crops, water
3. Terrain faces/embankments and shadows
4. Lower structures and trunks
5. Characters and objects, Y-sorted by their ground anchor
6. Upper canopies, roof overhangs, foreground details as needed
7. Weather, light effects, and UI

Avoid baking gameplay-dependent shadows, crop growth, or collision indicators into unrelated sprites.

## Quality bar / acceptance checklist
- Looks coherent beside already approved sprites at **actual gameplay scale**.
- Has correct orientation, light direction, palette, and perspective.
- Silhouette remains readable on a phone.
- Transparent background is truly transparent.
- Edges are clean; no cropped roof, branches, or animation frames.
- File dimensions, anchor, logical footprint, layers, and license/provenance are documented.
- Test in-game before marking APPROVED. Concept art is NOT a production-ready sprite.

## Workflow and authority
1. Art Studio proposes a brief and generates candidate art.
2. Review at native scale and in a mock gameplay screenshot.
3. Clean/export the exact PNG(s), verify alpha and pixel dimensions.
4. Commit under `assets/` and register in `ASSET_MANIFEST.md`.
5. Game Development integrates and tests on iPhone.
6. Only then mark asset APPROVED.
GitHub files are the shared source of truth across chats. A chat's remembered decisions are not authoritative unless reflected here. Record revisions in Git commits.

## Initial priorities
1. **A001 farmhouse**: correct roof geometry; warm, rustic, three-quarter silhouette.
2. A002 terrain base and paths: seamless, organic ground.
3. A003 hardwood and pine trees: believable layering.
4. A004 farmer: clear directions and consistent anchor.
5. A005 stones, weeds, ferns, wildflowers.
6. A006 creek and embankment set.

## Known current state
v0.3 uses procedural Canvas shapes, not imported sprite assets. Farmer/trees overlap and northern decorative ridgeline were observed working. Farmhouse roof is visibly wrong (open green triangle); overall look is still far below target concept art. Do not represent generated scene concepts as actual implemented game graphics.

# A002 Terrain v0.3 — experimental status

The local prototype now uses overlapping source-image patches, seeded selection, world-space masks, and pixel-scale transition fringe to create 512x384 previews from the A002 candidate artwork. Two deterministic seeds were rendered locally. These are **CANDIDATE previews**, not approved reusable autotiles.

## Findings
- Initial overlap implementation left black gaps; corrected in local prototype.
- Generated previews are continuous but still visually busy, and patch seams need inspection.
- Source artwork required recropping from the original presentation sheet to avoid baked grid borders.
- A separate mobile browser preview prototype was created locally; it uses a lightweight JS approximation, not the Python artwork quilting algorithm.

## Remaining integration
1. Commit the tested Python v0.3 generator and clean source PNG using a binary-capable upload path.
2. Add the mobile terrain lab page to the published GitHub Pages branch, and connect it to genuine generated candidate previews.
3. Run GitHub Actions on the committed A002 input and verify artifact output.
4. Add repeatable seam and visual checks, then obtain iPhone approval before updating ASSET_MANIFEST.md to READY or APPROVED.

No changes to the live game were made by this experiment.

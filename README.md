# HUD Ballistic Trajectory Overlay DX11 Occlusion

A DX11 compatibility and obstacle-occlusion edition of **HUD Ballistic Trajectory Overlay v6** for HELLDIVERS 2. This publishes the previously completed, in-game-tested package unchanged.

**[Download the final release](https://github.com/NeverB0re/HD2-HUD-Ballistic-Trajectory-DX11/releases/tag/v6-dx11-occlusion)** · [한국어 설명](docs/README_KO.md)

## Changes from the original v6

- Draws the local player's trajectory through a DX11-compatible screen GUI path.
- Hides trajectory sections behind obstacles using the original validated native scene-query interface.
- Retains the established thin line, grenade/throwable behavior and long-arc coverage.
- Removes the local throwable distance label as requested.
- Preserves the original ballistic calculations, supported-weapon catalogue and other packaged resources.

This is a compatibility edition, not a new ballistic model. It does not make every game weapon supported. The original v6 weapon/throwable catalogue and configurable features remain in the source.

## Installation

1. Completely close HELLDIVERS 2, including any background process.
2. Disable the original overlay and other DX11 trial/overlay editions.
3. Import `HUD_Ballistic_Trajectory_Overlay_DX11_Occlusion.zip` into Arsenal and enable Overlay.
4. Purge, Deploy, then launch with `--use-d3d11`.

The preserved package includes its original unified addon-discovery loader; it does not require adding a separate loader just for this overlay. When another pack also provides this overlay, avoid deploying both copies and give this edition the appropriate priority.

`HUDBTO.ini` is created beside the game's data folder if missing and read at mission start. Existing settings are preserved. `dx11_gui_lines=true` under `[overlay]` is the manual DX11 drawing option if automatic detection fails; changing a setting alone does not repair an outdated payload.

The installable file is the release asset, not GitHub's automatic source-code ZIP.

## Occlusion cost and validation

The added visibility pass is bounded to **32 native-query samples per drawn guide**. It samples along the whole guide and can reuse a result for up to three nearly unchanged draw calls. No extra visibility query is made while the guide is inactive. This does **not** disable the original non-ADS throwable behavior or unrelated original optional effects.

The native-query handoff is accepted only after the original build/world/preset/result checks succeed. This is sampled occlusion rather than GPU depth-buffer clipping; very small or rapidly changing obstacles and cached visibility have the normal limits of that approach.

The user confirmed that trajectories rendered in DX11 and were hidden behind obstacles. Offline checks passed for Lua syntax, archive structure, eight unchanged resources, query limits, cache reuse and fallback. The synthetic fixture used 25 queries for a 600-point guide; this is not an FPS benchmark. **No same-scene frame-time comparison was performed.**

Development validation used Steam build **25480438**. Native signatures are validated at runtime; compatibility with arbitrary later game updates is not promised.

Status log: `%LOCALAPPDATA%\CowboyBingus\Helldivers2\Logs\HUDBTO-Sparse.log`. `NATIVE_QUERY_ACTIVE` means the query path activated; it does not measure performance.

## Source and build

- `src/gun_calibration.lua`: exact UTF-8 Lua embedded in the final release.
- `docs/dx11_changes.diff`: changes against the supplied unmodified v6 Lua.
- `manifest.json`: exact release manifest.
- `dist/`: original completed Arsenal ZIP, also attached to the release.
- `build.py`: rebuilds the package, preserving the other resources from that ZIP.
- `verify_release.py`: verifies SHA-256, manifest, exact embedded source and preserved resource checksums using Python's standard library.

```console
python verify_release.py
python build.py --output dist/rebuilt.zip
python verify_release.py --package dist/rebuilt.zip
```

Rebuilding depends on the bundled reference ZIP as the template for unchanged original resources; it does not reconstruct those assets from Lua alone. The archived ZIP remains the canonical release if a different compression implementation changes its binary checksum.

## Origin and attribution

Based on the supplied **HUD Ballistic Trajectory Overlay v6** package, with a focused DX11 rendering/occlusion modification. The original overlay, weapon catalogue and embedded discovery/compatibility resources retain their original authorship. Bingus compatibility is preserved. No new license is imposed on third-party material by this repository. This is an independent compatibility edition, not an official Arrowhead release.

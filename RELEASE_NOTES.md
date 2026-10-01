# Final DX11 occlusion edition (based on v6)

The previously completed **HUD Ballistic Trajectory Overlay DX11 Occlusion** package, published unchanged.

- DX11-compatible local trajectory drawing and obstacle occlusion.
- Thin line, grenade/throwable behavior and long-arc coverage retained.
- Local throwable distance numbers removed.
- Added visibility pass capped at 32 native-query samples per guide, with short-lived cache reuse.
- Original ballistic model, supported catalogue, loader and other resources preserved.

**Install:** Disable the original overlay and trial editions, import the attached mod ZIP into Arsenal, enable Overlay, Purge / Deploy and launch with `--use-d3d11`.

**설치:** 게임 완전 종료 → 원본·시험판 비활성화 → 첨부 ZIP을 Arsenal에 가져오기 → Overlay 활성화 → Purge / Deploy → DX11로 실행.

The user confirmed in-game obstacle occlusion. Package, Lua syntax, resource-preservation and synthetic query/cache checks passed. No controlled FPS/frame-time benchmark was performed. Development validation used Steam build 25480438; future-build compatibility is not guaranteed.

GitHub automatic source-code ZIPs are not installable Arsenal packages.

SHA-256: `03a06f04de78a8bf20fec81e93355afc4a0ad2f566207fa204032d7b09a62d73`

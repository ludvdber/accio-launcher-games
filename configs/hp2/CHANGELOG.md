# Changelog — Harry Potter et la chambre des secrets

## v1.0 — 2026-03-28

### Renderer
- Renderer darknovismc D3D11 v1.6.2 (`d3d11drv.dll`) intégré
- Antialiasing 8x, filtrage anisotrope 16x
- Bump mapping, Parallax Occlusion Mapping
- SSAO (occlusion ambiante)
- SSR (réflexions d'écran)
- Vue illimitée (UnlimitedViewDistance)
- Détail de maillage complet à toute distance (FullMeshLOD)

### Compatibilité Windows moderne
- Mode borderless windowed — alt-tab sans crash
- FastAltTab activé
- Cap 100 FPS
- Suppression SafeDisc — aucun crack nécessaire

### Affichage
- Widescreen 16:9 (1920×1080) avec FOV 106°
- Interface mise à l'échelle (GUIScale=2.25) — compense l'UI conçue pour 640×480

### Audio / Langue
- Voix et textes français inclus
- Langue active par défaut : français

### Nettoyage
- Suppression DRM SafeDisc (secdrv.sys, drvmgt.dll, sx.exe)
- Suppression installeurs EA et launcher (Harry_Potter_Settings.exe)
- Suppression renderers legacy (D3DDrv, SoftDrv, SglDrv)
- Suppression polices asiatiques inutilisées
- Suppression textures multilingues inutilisées (MenuArt 21 langues)
- Suppression textures obsolètes (Old textures/, AOLDemo)
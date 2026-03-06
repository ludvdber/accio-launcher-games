# Changelog — Harry Potter à l'École des Sorciers

## v1.0 — 2026-03-06

### Renderer
- Renderer Kentie D3D11 (`d3d11drv.dll`) intégré — remplace DGVoodoo (incompatible avec HP1)
- Antialiasing 4x, filtrage anisotrope 16x
- Bump mapping, Parallax Occlusion Mapping
- HDR avec tonemapping filmic
- SSAO (occlusion ambiante)
- SSR (réflexions d'écran)
- Vue illimitée (UnlimitedViewDistance)

### Compatibilité Windows moderne
- Mode borderless windowed — alt-tab sans crash (fullscreen exclusif UE1 cassé sur Windows 10/11)
- FastAltTab activé
- Cap 100 FPS (limite recommandée UE1 — physique liée au framerate)

### Affichage
- Widescreen 16:9 (1920×1080) avec FOV 106°
- Interface mise à l'échelle (GUIScale=2.25) — compense l'UI conçue pour 640×480

### Audio / Langue
- Voix et textes français inclus
- Voix et textes anglais inclus (fichiers .int et AllDialog.uax)
- Langue active par défaut : français

### Nettoyage
- Suppression DRM SafeDisc (secdrv.sys, drvmgt.dll)
- Suppression installeurs EA, launcher abandonware, manuel PDF (43 Mo)
- Suppression polices asiatiques inutilisées
- Fichiers Help/*.bmp recréés vides (requis par le moteur au démarrage)
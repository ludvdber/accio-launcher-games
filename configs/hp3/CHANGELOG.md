# Changelog — Harry Potter et le Prisonnier d'Azkaban (HP3)

## v1.1 (2025-03-06)

### DGVoodoo 2.8.1 → 2.86.5
- Mise à jour majeure du wrapper graphique
- Anti-aliasing 4x (lissage des bords)
- Filtrage anisotrope 8x (textures plus nettes en angle)
- Mipmapping bilinéaire (transitions de textures plus douces)
- Résolution native automatique (Resolution = max)
- VSync activé (suppression des déchirures d'image)
- Upscaling Lanczos-2 (meilleure qualité de mise à l'échelle)
- Accès mémoire vidéo rapide (FastVideoMemoryAccess)
- Cap 60 FPS intégré via DGVoodoo (stabilité du gameplay, corrige le bug de l'Imp gelé)
- Watermark DGVoodoo désactivé
- Mode fenêtré étiré avec ratio préservé (stretched_ar)

### Widescreen 16:9
- Résolution 1920x1080 supportée (via hppoa.ini)
- Champ de vision (FOV) ajusté à 106.26° pour le 16:9
- Plus de vision sur les côtés au lieu de bandes noires
- Vidéos d'intro adaptées au widescreen

### Nettoyage des fichiers
- Suppression du dossier Support/ (installeur EA, enregistrement, EULA, fichiers d'aide)
- Suppression de eauninstall.exe (désinstalleur EA)
- Suppression de filelist.txt (liste de fichiers installeur)
- Suppression de system/pixomatic_debug.dll (renderer debug)
- Suppression de system/DefUnrealEd.ini, UDNHelpTopics.ini, UnrealEdTips.ini (config éditeur)
- Suppression de music/*.sfap0, music/*.sfk (fichiers de projet audio)
- Suppression de help/Unreal.ico
- ~15 Mo récupérés

### Fichiers conservés pour le modding
- Editor.dll, Editor.u, Editor.int (UnrealEd)
- Toutes les textures, maps, animations, sons, static meshes


## v1.0 (2025-03-05)

### Version initiale
- Version originale du jeu (source Abandonware France)
- DGVoodoo 2.8.1 intégré (config par défaut)
- Paramètres graphiques par défaut
- Résolution 4:3 (1280x960)
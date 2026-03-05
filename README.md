<div align="center">

# ⚡ Accio Launcher — Catalogue de Jeux

### Archives et configurations des jeux Harry Potter PC

[![Jeux disponibles](https://img.shields.io/badge/jeux_disponibles-1%2F6-d4a017?style=for-the-badge&labelColor=0d0d1a)]()
[![DGVoodoo](https://img.shields.io/badge/DGVoodoo-2.86.5-blue?style=for-the-badge&labelColor=0d0d1a)]()
[![Launcher](https://img.shields.io/badge/launcher-AccioLauncher-27ae60?style=for-the-badge&labelColor=0d0d1a)](https://github.com/ludvdber/AccioLauncher)

*Ce repo contient le catalogue et les archives des jeux utilisés par [Accio Launcher](https://github.com/ludvdber/AccioLauncher).*

</div>

---

## 📦 Comment ça fonctionne

Ce repo sert de **source de données** pour Accio Launcher :

- **`games.json`** — Le catalogue maître que le launcher télécharge au démarrage pour connaître les jeux disponibles, leurs versions et les URLs de téléchargement
- **Releases** — Les archives `.7z` des jeux sont hébergées en pièces jointes des releases GitHub
- **`configs/`** — Historique des configurations DGVoodoo et fichiers .ini par jeu

Le launcher vérifie automatiquement ce repo au démarrage. Quand une mise à jour est publiée ici, tous les launchers la détectent.

---

## 🎮 Jeux disponibles

| Jeu | Version | DGVoodoo | Widescreen | Statut |
|-----|---------|----------|------------|--------|
| ⚡ HP et le Prisonnier d'Azkaban (2004) | v1.1 | 2.86.5 | 16:9 (1920x1080) | ✅ En ligne |
| ⚡ HP à l'École des Sorciers (2001) | — | — | — | 🔜 À venir |
| ⚡ HP et la Chambre des Secrets (2002) | — | — | — | 🔜 À venir |
| ⚡ HP et la Coupe de Feu (2005) | — | — | — | 🔜 À venir |
| ⚡ HP et l'Ordre du Phénix (2007) | — | — | — | 🔜 À venir |
| ⚡ HP et le Prince de Sang-Mêlé (2009) | — | — | — | 🔜 À venir |

---

## 📋 Contenu d'une archive de jeu

Chaque archive `.7z` contient le jeu prêt à jouer :

```
HP3/
├── config/          ← Fichiers .ini copiés vers Mes Documents par le launcher
│   ├── hppoa.ini   (résolution 1920x1080)
│   └── User.ini    (FOV 106.26 pour 16:9)
├── system/          ← Moteur du jeu + DGVoodoo
│   ├── hppoa.exe   (exécutable)
│   ├── dgVoodoo.conf, DDraw.dll, D3D8.dll...
│   └── ...
├── Animations/, maps/, Movies/, music/, sounds/, textures/
└── ...
```

---


## 🗂️ Structure du repo

```
accio-launcher-games/
├── games.json              ← Catalogue maître (lu par le launcher)
├── README.md
├── configs/                ← Historique des configs par jeu
│   └── hp3/
│       ├── dgVoodoo_v1.0_original.conf
│       ├── dgVoodoo_v1.1_optimized.conf
│       └── CHANGELOG.md
└── Releases (onglet GitHub)
    ├── hp3-v1.0 → hp3.7z
    └── hp3-v1.1 → hp3.7z
```

---

## 🆕 Comment une mise à jour fonctionne

1. Une nouvelle archive est préparée (ex: DGVoodoo mis à jour)
2. Une release est créée ici avec la nouvelle archive
3. `games.json` est mis à jour avec la nouvelle version
4. Au prochain lancement, Accio Launcher détecte la mise à jour
5. L'utilisateur choisit de mettre à jour ou de rester sur l'ancienne version
6. Le downgrade est possible si une mise à jour cause un problème

---

## ⚖️ Avertissement légal

Les archives hébergées dans ce dépôt sont destinées aux personnes possédant une copie légale originale des jeux concernés. Ces archives servent de remplacement pratique aux supports physiques (CD-ROM) qui peuvent être endommagés, perdus ou incompatibles avec les systèmes modernes.

Il est de votre entière responsabilité de vous assurer que vous disposez des droits nécessaires pour télécharger et utiliser ces fichiers dans votre juridiction.

Les jeux Harry Potter sont la propriété intellectuelle de Warner Bros. Entertainment Inc. et Electronic Arts Inc. Ce projet n'est ni affilié, ni approuvé, ni sponsorisé par ces entreprises.

Le développeur de ce dépôt ne peut être tenu responsable de l'utilisation qui est faite de ces fichiers par les utilisateurs. En téléchargeant ces fichiers, vous acceptez l'entière responsabilité de leur utilisation.

---

<div align="center">

*Utilisé par [⚡ Accio Launcher](https://github.com/ludvdber/AccioLauncher)*

</div>

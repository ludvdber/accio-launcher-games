<div align="center">

# ⚡ Accio Launcher — Catalogue de Jeux

### Archives et configurations des jeux Harry Potter PC

[![Jeux disponibles](https://img.shields.io/badge/jeux_disponibles-6%2F8-d4a017?style=for-the-badge&labelColor=0d0d1a)]()
[![Catalogue](https://img.shields.io/badge/catalog__version-0.16-27ae60?style=for-the-badge&labelColor=0d0d1a)]()
[![Langues](https://img.shields.io/badge/langues-FR%20·%20EN%20·%20ES-9b59b6?style=for-the-badge&labelColor=0d0d1a)]()
[![Launcher](https://img.shields.io/badge/launcher-AccioLauncher-3776ab?style=for-the-badge&labelColor=0d0d1a)](https://github.com/ludvdber/AccioLauncher)

*Ce repo contient le catalogue et les archives des jeux utilisés par [Accio Launcher](https://github.com/ludvdber/AccioLauncher).*

</div>

---

## 📦 Comment ça fonctionne

Ce repo sert de **source de données** pour Accio Launcher :

- **`games.json`** — Le catalogue maître que le launcher télécharge au démarrage pour connaître les jeux disponibles, leurs versions et les URLs de téléchargement
- **Releases** — Les archives `.7z` des jeux sont hébergées en pièces jointes des releases GitHub
- **`configs/`** — Historique des configurations DGVoodoo et fichiers .ini par jeu

Le launcher vérifie automatiquement ce repo au démarrage. Quand une mise à jour est
publiée ici, tous les launchers la détectent — **sans qu'une nouvelle version du
launcher soit publiée**. C'est le principe : le catalogue vit sa propre vie.

---

## 🎮 État du catalogue

| # | Jeu | ID | Année | Archive | État |
|:-:|-----|:--:|:-----:|:-------:|:----:|
| I | Harry Potter à l'École des Sorciers | `hp1` | 2001 | 431 Mo | ✅ En ligne |
| II | Harry Potter et la Chambre des Secrets | `hp2` | 2002 | 463 Mo | ✅ En ligne |
| III | Harry Potter et le Prisonnier d'Azkaban | `hp3` | 2004 | 775 Mo | ✅ En ligne |
| IV | Harry Potter et la Coupe de Feu | `hp4` | 2005 | 1,7 Go | ✅ En ligne |
| V | Harry Potter et l'Ordre du Phénix | `hp5` | 2007 | 4,6 Go | ✅ En ligne |
| VI | Harry Potter et le Prince de Sang-Mêlé | `hp6` | 2009 | 4,4 Go | ✅ En ligne |
| VII | Reliques de la Mort — Partie 1 | `hp7a` | 2010 | ~5 Go | 🔜 Déclaré, pas d'archive |
| VIII | Reliques de la Mort — Partie 2 | `hp7b` | 2011 | ~5,5 Go | 🔜 Déclaré, pas d'archive |

Un jeu dont les `versions` ont `download_url` et `download_parts` à `null` s'affiche
dans le launcher en **« Bientôt disponible »** : il est visible, décrit et traduit,
mais son bouton de téléchargement est inactif. C'est voulu — le catalogue annonce ce
qui arrive.

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

Le chemin déclaré dans `executable` est **relatif à la racine de l'archive** et
validé au parsing par le launcher : pas de `..`, pas de chemin absolu, pas de lettre
de lecteur. Une entrée qui viole ces règles est rejetée, jeu compris — c'est ce qui
empêche un catalogue trafiqué de faire lancer n'importe quoi.

---

## 🗂️ Structure du repo

```
accio-launcher-games/
├── games.json              ← Catalogue maître (lu par le launcher)
├── README.md
├── configs/                ← Historique des configs par jeu
│   ├── hp1/  (HP.ini, User.ini, CHANGELOG.md)
│   ├── hp2/  (Game.ini, User.ini, CHANGELOG.md)
│   └── hp3/  (dgVoodoo.conf, dgVoodoo_v1.0_original.conf, CHANGELOG.md)
└── Releases (onglet GitHub)
    ├── hp3-v1.0 → hp3.7z
    └── hp3-v1.1 → hp3.7z
```

---

## 🆕 Comment une mise à jour fonctionne

1. Une nouvelle archive est préparée (ex: DGVoodoo mis à jour)
2. Une release est créée ici avec la nouvelle archive
3. `games.json` est mis à jour avec la nouvelle version
4. **Les traductions sont régénérées** (voir ci-dessous)
5. `catalog_version` est incrémenté — sinon les launchers déjà en cache ignorent le fichier
6. Au prochain lancement, Accio Launcher détecte la mise à jour
7. L'utilisateur choisit de mettre à jour ou de rester sur l'ancienne version
8. Le downgrade est possible si une mise à jour cause un problème

> ⚠️ **`catalog_version` doit être STRICTEMENT supérieur** à celui en cache pour
> qu'un launcher relise le fichier. Oublier de l'incrémenter est l'erreur classique :
> tout semble correct côté dépôt, et rien ne bouge côté utilisateurs.

### 🔐 Empreintes SHA-256 : ne les recopiez pas à la main

Le launcher vérifie chaque archive téléchargée. **Il n'a pas besoin que vous
saisissiez l'empreinte** : GitHub publie la sienne pour chaque pièce jointe de
release, et le launcher la récupère automatiquement dans la réponse qu'il reçoit
déjà pour les compteurs de téléchargement — aucune requête supplémentaire.

Les champs `sha256` et `sha256_parts` du catalogue sont **réservés aux archives
hébergées ailleurs que sur GitHub**. Une empreinte saisie à la main peut être fausse
ou oubliée, et une empreinte fausse est pire que pas d'empreinte : elle inspire une
confiance qu'elle ne mérite pas.

Pour la même raison, soyons clairs sur ce que cette vérification protège : elle
détecte une **corruption de transport** (téléchargement tronqué, proxy, disque qui
ment). Elle ne protège pas d'une archive remplacée à la source, puisque c'est GitHub
qui atteste ce que GitHub stocke.

---

## 🌍 Traductions du catalogue

Depuis la **v0.16**, chaque jeu et chaque version portent un bloc `i18n` qui
traduit les champs visibles par l'utilisateur — `name`, `description`, `tags` et
`changes`. Les champs techniques (URLs, tailles, `executable`, `ini_patches`…)
n'y figurent jamais.

```json
{
  "name": "Harry Potter à l'École des Sorciers",
  "tags": ["Aventure", "Action"],
  "i18n": {
    "en": { "name": "Harry Potter and the Philosopher's Stone",
            "tags": ["Adventure", "Action"] },
    "es": { "name": "Harry Potter y la piedra filosofal",
            "tags": ["Aventura", "Acción"] }
  }
}
```

Les traductions vivent **ici** et non dans le launcher, parce que ce catalogue se
met à jour à distance, indépendamment des releases : un jeu ajouté doit pouvoir
arriver déjà traduit, sans republier l'exécutable.

Le français reste la source. Une langue absente, ou un champ absent d'une langue,
retombe simplement sur le français — une traduction partielle ne casse rien.

### Régénérer après une modification

Depuis le dépôt du launcher :

```bash
python tools/apply_catalog_i18n.py ../accio-launcher-games/games.json
```

Le script est **idempotent** (rejouable sans dupliquer), préserve la mise en
forme du fichier, et **liste les chaînes françaises qu'il ne sait pas traduire**.
S'il en signale, ajoutez-les à ses dictionnaires puis relancez-le : c'est le
garde-fou qui évite qu'un nouveau jeu ou une nouvelle ligne de changelog reste
en français pour les anglophones et les hispanophones.

> Écrivez toujours le JSON avec `ensure_ascii=False`. Sinon les accents partent en
> `\uXXXX`, le fichier devient illisible en revue de PR, et plus personne ne peut
> contribuer une correction.

---

## 🔁 Rester synchrone avec le launcher

Le launcher embarque une copie de `games.json` (`src/data/games.json`) qui sert de
**repli toujours disponible** : premier lancement sans réseau, GitHub en panne,
utilisateur hors ligne. Entre l'embarqué et le distant, **le `catalog_version` le
plus élevé gagne**.

Les deux fichiers doivent donc rester alignés. Un chemin `executable` corrigé ici
mais pas là-bas produit un échec de lancement silencieux chez qui n'a pas encore
reçu le catalogue distant.

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

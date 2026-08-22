<div align="center">

# ⚡ Accio Launcher — Catalogue de Jeux

### Archives et configurations des jeux Harry Potter PC

[![Jeux disponibles](https://img.shields.io/badge/jeux_disponibles-8%2F8-d6a72c?style=for-the-badge&labelColor=0d0d1a)]()
[![Catalogue](https://img.shields.io/badge/catalog__version-0.18-27ae60?style=for-the-badge&labelColor=0d0d1a)]()
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

| # | Jeu | ID | Année | Release | Téléchargement | Installé | État |
|:-:|-----|:--:|:-----:|:-------:|:--------------:|:--------:|:----:|
| I | Harry Potter à l'École des Sorciers | `hp1` | 2001 | `hp1-v1.1` | 243 Mo | 431 Mo | ✅ En ligne |
| II | Harry Potter et la Chambre des Secrets | `hp2` | 2002 | `hp2-v1.0` | 247 Mo | 463 Mo | ✅ En ligne |
| III | Harry Potter et le Prisonnier d'Azkaban | `hp3` | 2004 | `hp3-v1.1` | 337 Mo | 775 Mo | ✅ En ligne |
| IV | Harry Potter et la Coupe de Feu | `hp4` | 2005 | `hp4-v1.0` | 847 Mo | 1,7 Go | ✅ En ligne |
| V | Harry Potter et l'Ordre du Phénix | `hp5` | 2007 | `hp5-v1.1` | 2,5 Go | 4,6 Go | ✅ En ligne |
| VI | Harry Potter et le Prince de Sang-Mêlé | `hp6` | 2009 | `hp6-v1.0` | 2,1 Go | 4,4 Go | ✅ En ligne |
| VII | Reliques de la Mort — Partie 1 | `hp7a` | 2010 | `hp7-v1.0` | 4,4 Go | 4,4 Go | ✅ En ligne |
| VIII | Reliques de la Mort — Partie 2 | `hp7b` | 2011 | `hp8-v1.0` | 7,5 Go | 7,5 Go | ✅ En ligne |

> **Téléchargement** est le poids réel des pièces jointes, relevé sur l'API GitHub.
> **Installé** est le `size_mb` déclaré dans le catalogue. Ne confondez jamais les
> deux : le launcher exige la somme des deux pendant l'installation, l'archive et
> les fichiers extraits cohabitant jusqu'au nettoyage final.

> ⚠️ **`size_mb` est la taille INSTALLÉE**, pas celle de l'archive. Le poids du
> téléchargement n'a pas à être saisi : le launcher le lit sur GitHub, dans la
> même réponse que les compteurs et les empreintes.

**Le catalogue est complet depuis la v0.18** : les huit jeux de la saga sont
téléchargeables, et les onze versions publiées portent toutes une empreinte
SHA-256 fournie par GitHub.

Le mécanisme d'annonce reste disponible pour la suite : un jeu dont les `versions`
ont `download_url` et `download_parts` à `null` s'affiche dans le launcher en
**« Bientôt disponible »** — visible, décrit et traduit, mais bouton inactif. C'est
voulu : le catalogue annonce ce qui arrive avant de le livrer.

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

La racine de l'archive **ne suit pas forcément l'identifiant du jeu** : `hp7a` est
livré par la release `hp7-v1.0`, dont l'archive `hp7.7z` se déploie dans `HP7/` ;
`hp7b` vient de `hp8-v1.0` et se déploie dans `HP8/`. C'est le nom historique du
dossier de jeu qui fait foi, pas l'identifiant du catalogue — d'où l'importance de
relire `executable` après avoir empaqueté une archive.

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
└── Releases (onglet GitHub)          ← 11 releases, une par version
    ├── hp1-v1.0, hp1-v1.1 → hp1.7z
    ├── hp3-v1.0, hp3-v1.1 → hp3.7z
    ├── hp5-v1.0, hp5-v1.1 → hp5.7z.001 … .002   (multi-volumes)
    ├── hp7-v1.0           → hp7.7z.001 … .003
    ├── hp8-v1.0           → hp8.7z.001 … .004
    └── trailers-v1        → hp1_video.mp4, hp3_video.mp4   (bandes-annonces)
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

## 📺 Bandes-annonces

Depuis la **1.0**, les vidéos ne sont **plus embarquées dans l'exécutable**. Deux
d'entre elles suffisaient à le faire passer de 74 à **160 Mo** ; les huit
l'auraient mené au-delà de 500 Mo, pour un ornement dont tout le monde ne veut
pas. Elles sont donc publiées ici, en pièces jointes de release, et le launcher
les propose au premier lancement (case cochable, poids annoncé) puis dans
**Paramètres → Affichage**, où l'on peut les ajouter ou les supprimer.

### Nom des fichiers

Une pièce jointe par jeu, nommée d'après l'**identifiant du catalogue** :

| Jeu | Fichier à publier |
|---|---|
| HP1 — École des Sorciers | `hp1_video.mp4` |
| HP2 — Chambre des Secrets | `hp2_video.mp4` |
| HP3 — Prisonnier d'Azkaban | `hp3_video.mp4` |
| HP4 — Coupe de Feu | `hp4_video.mp4` |
| HP5 — Ordre du Phénix | `hp5_video.mp4` |
| HP6 — Prince de Sang-Mêlé | `hp6_video.mp4` |
| HP7 — Reliques de la Mort, partie 1 | `hp7a_video.mp4` |
| HP7 — Reliques de la Mort, partie 2 | `hp7b_video.mp4` |

> ⚠️ C'est l'identifiant du **catalogue**, pas celui de l'archive. `hp7b` est
> livré par la release `hp8-v1.0`, dans une archive `hp8.7z` — mais sa
> bande-annonce s'appelle bien `hp7b_video.mp4`.

Format : **MP4 (H.264 + AAC)**, c'est ce que lit Qt Multimedia sans codec
supplémentaire. La vidéo est peinte en fond de fiche, donc pas de sous-titres
incrustés ni de logo dans un coin : le titre et les boutons passent par-dessus.

### Créer la release

| Champ | Valeur |
|---|---|
| **Tag** | `trailers-v1` |
| **Cible** | `main` |
| **Titre** | Bandes-annonces — v1 |
| **Brouillon** | non — voir ci-dessous |

Le **tag fait partie de l'URL de téléchargement**
(`…/releases/download/<tag>/<fichier>`) : il doit correspondre exactement à ce
que `games.json` déclare. Le changer, c'est changer les huit URLs.

> ⚠️ **Une release en brouillon n'existe pas pour le launcher.** Ses pièces
> jointes ne sont servies qu'à un compte authentifié : le téléchargement répond
> 404 chez l'utilisateur, et l'API ne publie ni sa taille ni son empreinte.
> Publier pour de bon, ou ne pas déclarer le bloc.

Description — elle n'a aucun rôle technique, personne ne la lit depuis le
launcher ; elle sert à ce qu'on sache, dans six mois, ce qu'il y a dedans :

```markdown
Bandes-annonces des jeux du catalogue, téléchargées à la demande par Accio
Launcher et jouées en fond de fiche.

Elles ne sont plus embarquées dans l'exécutable depuis la 1.0 : deux d'entre
elles le faisaient passer de 74 à 160 Mo. Le launcher les propose au premier
lancement et dans Paramètres → Affichage, où l'on peut les ajouter ou les
supprimer à tout moment.

Ces fichiers ne sont pas nécessaires pour jouer.

Format : MP4 (H.264 + AAC). Un fichier par jeu, nommé d'après l'identifiant
du catalogue : hp1_video.mp4 … hp6_video.mp4, hp7a_video.mp4, hp7b_video.mp4.
```

### Écrire le bloc : `tools/sync_trailers.py`

**Ne remplissez pas le bloc à la main.** Une fois la release publiée, depuis le
dépôt du launcher :

```bash
python tools/sync_trailers.py src/data/games.json ../accio-launcher-games/games.json --bump
```

Il lit la release, y trouve les `<id>_video.mp4`, et écrit URL et `size_mb`
d'après ce qui y est **réellement publié** — dans les DEUX fichiers, qui doivent
rester identiques. Il préserve CRLF et indentation, il est rejouable, et il
signale les vidéos sans jeu correspondant comme les jeux sans vidéo.

`--tag trailers-v2` pour une autre release, `--version 2.0` pour re-versionner
tout le monde, `--bump` pour incrémenter `catalog_version` au passage.

### Le bloc `trailers` de `games.json`

```jsonc
"trailers": {
  "hp1": {
    "version": "1.0",
    "url": "https://github.com/ludvdber/accio-launcher-games/releases/download/trailers-v1/hp1_video.mp4",
    "size_mb": 82
  }
}
```

- **`version`** — c'est elle qui déclenche un re-téléchargement. Le fichier est
  rangé chez l'utilisateur sous `hp1_video_v1.0.mp4` : tant que la version ne
  bouge pas, rien n'est retéléchargé ; dès qu'elle change, l'ancienne est
  supprimée et la nouvelle arrive. **Sans ce numéro, une bande-annonce améliorée
  ne remplacerait jamais l'ancienne**, puisque le nom de la pièce jointe, lui,
  ne change pas.
- **N'y déclarez que ce qui existe.** Huit entrées dont six répondent 404, ce
  sont six échecs à chaque tentative. Le catalogue se met à jour à distance :
  ajoutez les autres au fur et à mesure, sans republier le launcher.
- **`size_mb`** sert au libellé du bouton et au garde-fou de taille. Le poids
  réel publié par GitHub le remplace dès qu'il est connu.
- **Pas de `sha256` à la main**, même règle que les archives (voir plus haut).
- **`url` en https** — une autre valeur est écartée à la lecture.

### Améliorer une bande-annonce

1. Publier le nouveau fichier (même nom) dans une release — `trailers-v2` par
   exemple, ou en remplaçant la pièce jointe.
2. Rejouer `tools/sync_trailers.py` avec `--tag`, `--version` et `--bump` : il
   met à jour l'`url`, la taille, la `version` et `catalog_version` d'un coup.

À la main, ce serait quatre champs à changer sans en oublier un, dans deux
fichiers qui doivent rester identiques.

L'ancien fichier est supprimé du disque de l'utilisateur avant que le nouveau ne
soit téléchargé — le dossier ne grossit pas à chaque révision.

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

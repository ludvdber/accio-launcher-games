"""Vérifie games.json AVANT qu'il n'atteigne les joueurs.

Un envoi sur main est servi tel quel à chaque launcher : une erreur ici n'est pas
« à corriger plus tard », elle est chez tout le monde dans l'heure. Le script lit
donc le catalogue avec le CODE DU LAUNCHER (dépôt AccioLauncher extrait à côté),
et non avec une copie de ses règles : une règle recopiée finit par diverger.

Deux modes :

    python tools/verifier_catalogue.py games.json --launcher ../AccioLauncher [--precedent ancien.json]
    python tools/verifier_catalogue.py games.json --liens

Le premier refuse, entre autres, un catalogue modifié sans hausse de
`catalog_version` : « le plus grand gagne », donc un envoi à version égale
n'atteindrait personne (payé le 2026-09-23, 0.26 contre 0.27 déjà publiée). Le
second vérifie que chaque adresse répond et que les tailles déclarées tiennent
sous le plafond du téléchargeur.

Sortie : annotations GitHub (`::error`) et résumé du run ; code 1 au moindre
défaut. Aucune dépendance hors de la bibliothèque standard.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Le téléchargeur abandonne au-delà de la taille déclarée × ce facteur
# (AccioLauncher, src/core/downloader.py, SIZE_OVERHEAD_FACTOR).
FACTEUR_PLAFOND = 1.5
MIO = 1024 * 1024

erreurs: list[str] = []
avertissements: list[str] = []


def erreur(message: str) -> None:
    erreurs.append(message)
    print(f"::error file=games.json::{message}")


def avertir(message: str) -> None:
    avertissements.append(message)
    print(f"::warning file=games.json::{message}")


def resume(titre: str, lignes: list[str]) -> None:
    chemin = os.environ.get("GITHUB_STEP_SUMMARY")
    if not chemin:
        return
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(f"### {titre}\n\n")
        f.writelines(f"- {ligne}\n" for ligne in lignes)
        f.write("\n")


def lire(chemin: Path) -> tuple[str, dict]:
    texte = chemin.read_text(encoding="utf-8")
    return texte, json.loads(texte)


# --- Mode catalogue -------------------------------------------------------------------------------

class _Capture(logging.Handler):
    """Tout avertissement du parseur est un jeu, une langue ou une sauvegarde que le launcher JETTERAIT."""

    def __init__(self) -> None:
        super().__init__(logging.WARNING)
        self.messages: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.messages.append(record.getMessage())


def verifier_catalogue(chemin: Path, launcher: Path, precedent: Path | None) -> None:
    try:
        texte, brut = lire(chemin)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        erreur(f"games.json illisible : {exc}")
        return

    # Règle 56 du launcher : un accent écrit é rend le fichier illisible en revue.
    # Les caractères de contrôle (\u0000-\u001f) restent permis, JSON les exige échappés.
    for m in re.finditer(r"\\u(?!00[01][0-9a-fA-F])[0-9a-fA-F]{4}", texte):
        ligne = texte.count("\n", 0, m.start()) + 1
        erreur(f"ligne {ligne} : caractère échappé {m.group()} — écrire le caractère lui-même (ensure_ascii=False)")
        break

    if not isinstance(brut, dict):
        erreur("le catalogue doit être un objet JSON (format à clé `games`)")
        return

    sys.path.insert(0, str(launcher.resolve()))
    from src.core import game_data  # noqa: E402 — le launcher n'est connu qu'ici
    from src.core.version_utils import compare_versions  # noqa: E402

    capture = _Capture()
    logging.getLogger().addHandler(capture)
    logging.getLogger().setLevel(logging.WARNING)
    try:
        catalogue = game_data._parse_catalog(brut)
    except ValueError as exc:
        erreur(f"refusé par le launcher : {exc}")
        return
    finally:
        logging.getLogger().removeHandler(capture)
    for message in capture.messages:
        erreur(f"le launcher écarterait ceci : {message}")

    version = str(brut.get("catalog_version", ""))
    if not re.fullmatch(r"\d+(\.\d+)*", version):
        erreur(f"catalog_version « {version} » : attendu des nombres séparés par des points (ex. 0.32)")

    entrees = brut.get("games", [])
    if len(catalogue.games) != len(entrees):
        erreur(f"{len(entrees)} jeux déclarés, {len(catalogue.games)} lus par le launcher")
    if isinstance(brut.get("trailers"), dict) and len(catalogue.trailers) != len(brut["trailers"]):
        erreur(f"{len(brut['trailers'])} bandes-annonces déclarées, {len(catalogue.trailers)} lues")
    if isinstance(brut.get("contributors"), list) and len(catalogue.contributors) != len(brut["contributors"]):
        erreur(f"{len(brut['contributors'])} contributeurs déclarés, {len(catalogue.contributors)} lus")

    ids = [g.get("id") for g in entrees if isinstance(g, dict)]
    for doublon in sorted({i for i in ids if ids.count(i) > 1}):
        erreur(f"identifiant de jeu en double : {doublon}")
    for jeu in entrees:
        if not isinstance(jeu, dict):
            continue
        numeros = [v.get("version") for v in jeu.get("versions", []) if isinstance(v, dict)]
        for champ in ("latest_version", "recommended_version"):
            if jeu.get(champ) and jeu[champ] not in numeros:
                erreur(f"{jeu.get('id')} : {champ} = {jeu[champ]}, absente de ses versions {numeros}")
        for doublon in sorted({n for n in numeros if numeros.count(n) > 1}):
            erreur(f"{jeu.get('id')} : version {doublon} déclarée deux fois")
    for tid in (brut.get("trailers") or {}):
        if tid not in ids:
            avertir(f"bande-annonce « {tid} » sans jeu du même identifiant")

    lignes = [f"catalog_version {version}", f"{len(catalogue.games)} jeux lus par le launcher"]

    if precedent is not None:
        try:
            _, ancien = lire(precedent)
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            ancien = None
        if isinstance(ancien, dict) and ancien != brut:
            v_ancien = str(ancien.get("catalog_version", "0"))
            if compare_versions(version, v_ancien) <= 0:
                erreur(f"le catalogue change mais catalog_version reste {version} (avant : {v_ancien}). Le launcher "
                       f"garde la plus GRANDE version : sans hausse, ce changement n'atteindrait personne.")
            lignes.append(f"version précédente {v_ancien}")

    embarque = launcher / "src" / "data" / "games.json"
    if embarque.is_file():
        _, copie = lire(embarque)
        v_copie = str(copie.get("catalog_version", "0"))
        ecart = compare_versions(v_copie, version)
        if ecart == 0 and copie != brut:
            erreur(f"le launcher embarque une AUTRE version {version} : deux contenus sous un même numéro, les joueurs "
                   f"n'auraient pas tous le même catalogue. Aligner les deux copies, ou monter la version.")
        elif ecart > 0:
            avertir(f"le launcher embarque déjà la {v_copie}, plus récente que celle-ci ({version}) : ce dépôt est en retard")
        lignes.append(f"copie embarquée dans le launcher : {v_copie}")

    resume("Catalogue", lignes + [f"❌ {e}" for e in erreurs] + [f"⚠️ {a}" for a in avertissements])


# --- Mode liens ------------------------------------------------------------------------------------

def _adresses(noeud, chemin: str = "") -> list[tuple[str, str]]:
    """Toutes les chaînes http(s) du catalogue, traductions comprises, avec l'endroit où elles sont."""
    if isinstance(noeud, dict):
        return [a for k, v in noeud.items() for a in _adresses(v, f"{chemin}.{k}" if chemin else str(k))]
    if isinstance(noeud, list):
        return [a for i, v in enumerate(noeud) for a in _adresses(v, f"{chemin}[{i}]")]
    if isinstance(noeud, str) and re.match(r"(?i)https?://", noeud):
        return [(noeud, chemin)]
    return []


def _taille(url: str) -> int | None:
    """Taille réelle en octets (None si le serveur ne la dit pas). Lève sur un échec."""
    requete = urllib.request.Request(url, headers={"Range": "bytes=0-0", "User-Agent": "accio-launcher-games-ci"})
    with urllib.request.urlopen(requete, timeout=30) as reponse:
        plage = reponse.headers.get("Content-Range", "")
        if "/" in plage and plage.rsplit("/", 1)[1].isdigit():
            return int(plage.rsplit("/", 1)[1])
        longueur = reponse.headers.get("Content-Length")
        return int(longueur) if reponse.status == 200 and longueur and longueur.isdigit() else None


def verifier_liens(chemin: Path) -> None:
    _, brut = lire(chemin)
    tailles: dict[str, int | None] = {}
    vus: set[str] = set()
    for url, ou in _adresses(brut):
        if url in vus:
            continue
        vus.add(url)
        if not url.lower().startswith("https://"):
            erreur(f"{ou} : adresse non https, refusée par le launcher : {url}")
            continue
        try:
            tailles[url] = _taille(url)
        except urllib.error.HTTPError as exc:
            erreur(f"{ou} : {url} répond {exc.code}")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            erreur(f"{ou} : {url} injoignable ({exc})")

    # Plafond du téléchargeur : une taille déclarée trop basse fait AVORTER un téléchargement sain.
    for tid, t in (brut.get("trailers") or {}).items():
        reel = tailles.get(t.get("url")) if isinstance(t, dict) else None
        if reel and isinstance(t.get("size_mb"), (int, float)):
            if reel > t["size_mb"] * MIO * FACTEUR_PLAFOND:
                erreur(f"bande-annonce {tid} : {reel / MIO:.0f} Mo réels pour {t['size_mb']} déclarés — le "
                       f"téléchargement serait interrompu (plafond ×{FACTEUR_PLAFOND})")
            elif reel > t["size_mb"] * MIO:
                avertir(f"bande-annonce {tid} : {reel / MIO:.0f} Mo réels pour {t['size_mb']} déclarés "
                        f"(relancer tools/sync_trailers.py du launcher)")
    for jeu in brut.get("games", []):
        for v in jeu.get("versions", []) if isinstance(jeu, dict) else []:
            urls = v.get("download_parts") or ([v["download_url"]] if v.get("download_url") else [])
            reels = [tailles.get(u) for u in urls]
            if urls and all(reels) and isinstance(v.get("size_mb"), (int, float)):
                total = sum(reels)
                if total > v["size_mb"] * MIO * FACTEUR_PLAFOND:
                    erreur(f"{jeu.get('id')} {v.get('version')} : archive de {total / MIO:.0f} Mo pour size_mb "
                           f"{v['size_mb']} — sans la réponse de GitHub, le téléchargement serait interrompu")

    resume("Liens", [f"{len(vus)} adresses vérifiées"] + [f"❌ {e}" for e in erreurs]
           + [f"⚠️ {a}" for a in avertissements])


def main() -> int:
    # Les messages sont en français : sous Windows, la page de codes de la console les abîmerait.
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("catalogue", type=Path)
    parser.add_argument("--launcher", type=Path, help="dépôt AccioLauncher extrait (mode catalogue)")
    parser.add_argument("--precedent", type=Path, help="games.json d'avant ce changement")
    parser.add_argument("--liens", action="store_true", help="vérifier les adresses au lieu du contenu")
    args = parser.parse_args()
    if args.liens:
        verifier_liens(args.catalogue)
    elif args.launcher:
        verifier_catalogue(args.catalogue, args.launcher,
                           args.precedent if args.precedent and args.precedent.is_file() else None)
    else:
        parser.error("--launcher ou --liens")
    if not erreurs:
        print(f"OK ({len(avertissements)} avertissement(s))")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())

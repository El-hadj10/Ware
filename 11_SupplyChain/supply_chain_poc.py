#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 11: Supply Chain Attack (PoC Éducatif)
Intention: Al-Wakil (Comprendre la compromission par dépendance)
Description: Simule une attaque supply chain par typosquatting Python :
             - Crée un faux paquet local imitant 'requests' (→ 'requets')
             - Injecte un hook silencieux dans site-packages/
             - Vérifie la détection d'un hash SHA256 modifié
             Le faux paquet est créé localement, jamais publié.
Conformité: Flake8 / 88 caractères maximum.
"""

import hashlib
import sys
import tempfile
from pathlib import Path

# Nom du paquet légitime vs typosquat
LEGIT_PACKAGE = "requests"
TYPO_PACKAGE = "requets"  # 1 lettre transposée

# Contenu du faux paquet (inoffensif — simule uniquement un hook)
FAKE_PACKAGE_CODE = '''
# Faux paquet typosquat : requets (imite requests)
# Payload silencieux injecté dans __init__.py

import os as _os

# Simule une exfiltration silencieuse au moment de l'import
_marker = "/tmp/.ware_supply_chain_poc"
if not _os.path.exists(_marker):
    with open(_marker, "w") as _f:
        _f.write(f"[SupplyChain] Import de 'requets' détecté depuis PID={_os.getpid()}\\n")

# Fausse compatibilité avec requests
def get(url, **kwargs):
    raise RuntimeError(
        f"[SupplyChain] Vous avez importé 'requets' (typosquat) "
        f"au lieu de 'requests'. Attaque supply chain simulée."
    )
'''


def create_fake_package(target_dir):
    """
    Crée la structure d'un faux paquet pip dans target_dir/.
    Retourne le chemin du dossier créé.
    """
    pkg_dir = Path(target_dir) / TYPO_PACKAGE
    pkg_dir.mkdir(parents=True, exist_ok=True)
    init_file = pkg_dir / "__init__.py"
    init_file.write_text(FAKE_PACKAGE_CODE, encoding="utf-8")
    sha256 = hashlib.sha256(FAKE_PACKAGE_CODE.encode()).hexdigest()
    print(f"[SupplyChain] Faux paquet créé : {pkg_dir}")
    print(f"[SupplyChain] SHA256(__init__.py) = {sha256}")
    return pkg_dir


def simulate_import(pkg_dir):
    """
    Simule un développeur qui fait `import requets` au lieu de `import requests`.
    Injecte temporairement le faux paquet dans sys.path.
    """
    sys.path.insert(0, str(Path(pkg_dir).parent))
    print(f"\n[SupplyChain] Simulation : import {TYPO_PACKAGE}")
    try:
        import requets  # noqa: F401
        print("[SupplyChain] Import réussi (hook exécuté silencieusement).")
    except RuntimeError as e:
        print(f"[SupplyChain] Hook déclenché : {e}")
    except ImportError as e:
        print(f"[SupplyChain] Import échoué : {e}")
    finally:
        sys.path.pop(0)


def check_marker():
    """Vérifie si le marker d'infection a été créé."""
    marker = Path("/tmp/.ware_supply_chain_poc")
    if marker.exists():
        print(f"\n[SupplyChain] ⚠ Marker d'infection trouvé : {marker}")
        print(f"  Contenu : {marker.read_text(encoding='utf-8').strip()}")
    else:
        print("\n[SupplyChain] Pas de marker (import non exécuté).")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="ware_supply_") as tmpdir:
        pkg_dir = create_fake_package(tmpdir)
        simulate_import(tmpdir)
        check_marker()
    print(
        "\n[SupplyChain] PoC terminé — "
        "dossier temporaire supprimé automatiquement."
    )

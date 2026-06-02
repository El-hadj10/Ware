#!/usr/bin/env python3
"""
Script d'installation du hook pre-commit pour le laboratoire Ware.
- Vérifie la conformité flake8
- Valide la structure des agents Qodo
"""
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.resolve()
HOOKS = ROOT / ".git" / "hooks"
PRECOMMIT = HOOKS / "pre-commit"

HOOK_SCRIPT = """#!/bin/sh
flake8 .
if [ $? -ne 0 ]; then
  echo '\n❌ Erreur flake8 : corrige le code avant de committer.'
  exit 1
fi
python3 ./.qodo/workflows/validate_agents.py
if [ $? -ne 0 ]; then
  echo '\n❌ Erreur Qodo : agents non valides.'
  exit 1
fi
"""


def main():
    if not HOOKS.exists():
        print(f"Dossier hooks introuvable : {HOOKS}")
        return
    with open(PRECOMMIT, "w", encoding="utf-8") as f:
        f.write(HOOK_SCRIPT)
    os.chmod(PRECOMMIT, 0o755)
    print("✔ Hook pre-commit installé et prêt à protéger Ware !")


if __name__ == "__main__":
    main()

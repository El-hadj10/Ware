#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: .qodo/workflows
Description: Validation de la structure conforme des fichiers godo_agent.json.
Conformité: Flake8 / 88 caractères maximum.
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.resolve()
AGENTS_PATH = ROOT / ".qodo/agents"
MODULES = [
    "Keylogger",
    "Spyware",
    "Worm",
    "Ransomware",
    "Malware_IA",
    "Backdoor_C2",
    "Persistence",
    "PrivEsc",
    "Cryptominer",
    "Fileless",
    "SupplyChain",
]


def validate_agent(agent_path):
    """Vérifie la présence et la structure des clés requises dans le JSON."""
    try:
        with open(agent_path, encoding="utf-8") as f:
            data = json.load(f)
        assert "name" in data
        assert "description" in data
        assert "tasks" in data and isinstance(data["tasks"], list)
        for task in data["tasks"]:
            assert "title" in task
            assert "status" in task
        print(f"✔ {agent_path} : OK")
    except Exception as e:
        print(f"✘ {agent_path} : {e}")


def main():
    """Parcourt les modules pour valider chaque fichier godo_agent.json."""
    print("Validation des fichiers godo_agent.json...")
    for module in MODULES:
        agent_file = AGENTS_PATH / module / "godo_agent.json"
        if agent_file.exists():
            validate_agent(agent_file)
        else:
            print(f"✘ {agent_file} : Fichier manquant")


if __name__ == "__main__":
    main()
    
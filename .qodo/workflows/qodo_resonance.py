#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: .qodo/workflows
Description: Module de résonance chromatique individualisée selon le caractère.
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

# Séquences de couleurs ANSI standard
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"  # Couleur de l'armature et de la bannière

# Attribution des couleurs selon le caractère de chaque agent
AGENT_COLORS = {
    "Keylogger": "\033[93m",    # Jaune : Vigilance & Capture
    "Spyware": "\033[96m",      # Cyan : Omniscience & Regard
    "Worm": "\033[92m",         # Vert : Expansion & Structure du vivant
    "Ransomware": "\033[91m",   # Rouge : Force & Scellé immuable
    "Malware_IA": "\033[95m",   # Magenta/Violet : Mutation & Esprit hybride
    "Backdoor_C2": "\033[91m",  # Rouge : Connexion furtive & Canal caché
    "Persistence": "\033[33m",  # Orange : Racine & Ancrage
    "PrivEsc": "\033[93m",      # Jaune : Escalade & Lumière volée
    "Cryptominer": "\033[92m",  # Vert : Calcul & Ressource détournée
    "Fileless": "\033[95m",     # Magenta : Fantôme & Exécution sans trace
    "SupplyChain": "\033[96m",  # Cyan : Infiltration & Confiance trahie
}


def print_resonance_banner():
    """Affiche la bannière en Cyan avec une raw string (W605)."""
    banner = r"""
     ____                                                 
    |  _ \ ___  ___  ___  _ __   __ _ _ __   ___ ___  ___ 
    | |_) / _ \/ __|/ _ \| '_ \ / _` | '_ \ / __/ _ \/ __|
    |  _ <  __/\__ \ (_) | | | | (_| | | | | (_|  __/\__ \
    |_| \_\___||___/\___/|_| |_|\__,_|_| |_|\___\___||___/
    """
    print(f"{CYAN}{banner}{RESET}")


def calculate_metrics(tasks):
    """Calcule le ratio et le pourcentage de complétion des tâches."""
    if not tasks:
        return 0.0
    completed = sum(1 for t in tasks if t.get("status") == "Terminé")
    return (completed / len(tasks)) * 100.0


def main():
    """Affiche le rapport de résonance avec son infrastructure en couleur."""
    print_resonance_banner()
    print(f"{CYAN}" + "=" * 70 + f"{RESET}")
    print(f" {BOLD}{CYAN}[📊] RAPPORT DE RÉSONANCE ET D'ÉQUILIBRE SYMÉTRIQUE{RESET}")
    print(f"{CYAN}" + "=" * 70 + f"{RESET}")

    for module in MODULES:
        agent_file = AGENTS_PATH / module / "godo_agent.json"
        color = AGENT_COLORS.get(module, CYAN)

        if agent_file.exists():
            with open(agent_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            name = data.get("name", module)
            tasks = data.get("tasks", [])
            percentage = calculate_metrics(tasks)

            # Construction de la jauge avec la couleur propre à l'agent
            blocks_filled = int(percentage / 10)
            blocks_empty = 10 - blocks_filled
            gauge = f"{color}" + "█" * blocks_filled + f"{RESET}" + "░" * blocks_empty

            print(f"\n{BOLD}{color}[Agent]{RESET} {name}")
            print(f"Status : [{gauge}] {color}{percentage:.1f}%{RESET}")

            if percentage == 100.0:
                print(f" {color}✨ L'Ordre Harmonique règne sur ce module.{RESET}")
        else:
            print(f"\n{BOLD}{color}[Agent]{RESET} {module}")
            print(f" \033[91m✘ Fichier godo_agent.json introuvable.{RESET}")

    print("\n" + f"{CYAN}" + "=" * 70 + f"{RESET}")


if __name__ == "__main__":
    main()
    
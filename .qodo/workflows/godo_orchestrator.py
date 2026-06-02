#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: .qodo/workflows
Description: Orchestrateur central pour la gestion et la simulation des agents.
Conformité: Flake8 / 88 caractères maximum.
"""

import json
from pathlib import Path
from typing import Dict, List

# On part de .qodo/workflows, on remonte deux crans
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

STATUS_COLORS = {
    "À faire": "[ ]",
    "En cours": "[~]",
    "Terminé": "[✔]",
}


def discover_agents() -> List[Dict]:
    """Découvre et charge les fichiers JSON de configuration de chaque agent."""
    agents = []
    for module in MODULES:
        agent_file = AGENTS_PATH / module / "godo_agent.json"
        if agent_file.exists():
            with open(agent_file, encoding="utf-8") as f:
                try:
                    agent = json.load(f)
                    agent["_path"] = agent_file
                    agents.append(agent)
                except Exception as e:
                    print(f"Erreur lecture {agent_file}: {e}")
    return agents


def print_agent_summary(agent: Dict):
    """Affiche un résumé structuré des tâches et statuts d'un agent."""
    print("\n" + "=" * 60)
    print(f"Module : {agent.get('module')}")
    print(f"Nom    : {agent.get('name')}")
    print(f"Desc.  : {agent.get('description')}")
    print("Tâches :")
    for idx, task in enumerate(agent.get("tasks", []), 1):
        status = STATUS_COLORS.get(task["status"], task["status"])
        print(f"  {idx}. {status} {task['title']}")


def simulate_audit(agent: Dict):
    """Simule le cycle de vie d'une tâche d'audit (À faire -> En cours -> Terminé)."""
    print(f"\n--- Simulation d'audit pour {agent.get('name')} ---")
    tasks = agent.get("tasks", [])
    if not tasks:
        print("Aucune tâche à simuler.")
        return

    # On simule le passage de la première tâche à 'En cours', puis 'Terminé'
    orig_status = tasks[0]["status"]
    tasks[0]["status"] = "En cours"
    print_agent_summary(agent)
    
    input("\nAppuyez sur Entrée pour terminer la tâche...")
    tasks[0]["status"] = "Terminé"
    print_agent_summary(agent)
    
    # Restauration du statut initial pour ne pas altérer le fichier de base
    tasks[0]["status"] = orig_status


def main():
    """Point d'entrée principal de l'orchestrateur de sécurité."""
    print("\n==== GODO ORCHESTRATOR - AUDIT SÉCURITÉ ====")
    agents = discover_agents()
    if not agents:
        print("Aucun agent détecté.")
        return
    for agent in agents:
        print_agent_summary(agent)
    print("\n--- Simulation d'exécution ---")
    for agent in agents:
        simulate_audit(agent)


if __name__ == "__main__":
    main()
    
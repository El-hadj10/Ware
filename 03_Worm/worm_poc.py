#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 03: Worm / Ver Informatique (PoC Éducatif)
Intention: Al-Muhsi (Cartographier et dénombrer pour ne rien laisser dans l'ombre)
Description: Simule la découverte réseau (reconnaissance) et le mouvement latéral
             autonome (auto-réplication) au sein d'un sous-réseau virtuel local.
"""

import os
import shutil
import time

# Définition de notre infrastructure réseau virtuelle (simulée par des dossiers)
NETWORK_ROOT = "./virtual_network"
SUB_NETWORKS = [
    "192.168.1.10_Poste_Secretariat",
    "192.168.1.20_Serveur_Compta",
    "192.168.1.30_Poste_RH",
    "192.168.1.40_Serveur_Production",
]


def setup_virtual_network():
    """Génère l'infrastructure réseau locale pour le laboratoire."""
    print("[*] Configuration de l'infrastructure réseau virtuelle...")
    for node in SUB_NETWORKS:
        node_path = os.path.join(NETWORK_ROOT, node)
        os.makedirs(node_path, exist_ok=True)
    print("[✅] Réseau virtuel prêt pour l'analyse.\n")


def simulate_worm_propagation():
    """Simule le comportement autonome du ver : scan, ciblage et réplication."""
    print("=" * 60)
    print(" [!] Lancement du PoC Worm - Analyse Réseau Autonome ")
    print("=" * 60)

    # Le ver identifie l'emplacement actuel de son propre script
    current_script = __file__

    # Étape 1 : Reconnaissance & Dénombrement (Al-Muhsi)
    print(
        "[🔍 SCAN] Analyse des adresses IP actives sur le "
        "sous-réseau 192.168.1.0/24..."
    )
    time.sleep(1.5)

    nodes_found = os.listdir(NETWORK_ROOT)
    print(f"[📊 INFRASTRUCTURE] {len(nodes_found)} machines actives détectées.")

    # Étape 2 & 3 : Ciblage et Mouvement Latéral (Propagation)
    for node in nodes_found:
        node_path = os.path.join(NETWORK_ROOT, node)
        target_file_path = os.path.join(node_path, "worm_replicated.py")

        print(f"\n[➔] Tentative de connexion vers le nœud : {node}")
        time.sleep(0.5)

        # Vérification si la machine est déjà infectée (idempotence du ver)
        if os.path.exists(target_file_path):
            print(f"[•] Nœud {node} déjà analysé/infecté. Passage au suivant.")
        else:
            print(
                "[💥 EXPLOITATION] Connexion établie. "
                f"Copie autonome du code sur {node}..."
            )
            # Le ver se duplique lui-même sur la machine cible
            shutil.copy2(current_script, target_file_path)

            # Simulation de l'exécution et de l'activation d'un indicateur.
            with open(os.path.join(node_path, "status.txt"), "w") as f:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                f.write(
                    "Infecté de manière autonome le "
                    f"{timestamp}\n"
                )
            print(f"[✅ SUCCESS] Le ver est désormais actif et persistant sur {node}.")
            time.sleep(0.5)

    print("\n" + "=" * 60)
    print(" [✅] Fin de la simulation de mouvement latéral. ")
    print(f" Explore le dossier '{NETWORK_ROOT}' pour voir la propagation.")
    print("=" * 60)


if __name__ == "__main__":
    # 1. Génération de l'environnement réseau cloisonné
    setup_virtual_network()
    # 2. Exécution de la routine du ver
    simulate_worm_propagation()
    
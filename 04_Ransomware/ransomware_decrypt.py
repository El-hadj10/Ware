#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 04: Ransomware (PoC Cryptographique)
Intention: Al-Basit (Restauration de la liberté d'accès aux données)
Description: Lit la clé secrète locale pour rétablir les fichiers d'origine.
"""

import os
from cryptography.fernet import Fernet

VAULT_DIR = "./vault_documents"
KEY_FILE = "secret.key"


def execute_decryption():
    """Lit la clé enregistrée et restaure les fichiers à leur état initial."""
    print("=" * 60)
    print(" [!] Initialisation du PoC Ransomware - Phase [Al-Basit] ")
    print("=" * 60)
    if not os.path.exists(KEY_FILE):
        print(
            "[❌ ERREUR] Impossible de procéder : "
            "Clé 'secret.key' introuvable."
        )
        return

    # Étape 1 : Lecture de la clé secrète
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    # Étape 2 : Parcours et déchiffrement
    for root, dirs, files in os.walk(VAULT_DIR):
        for file in files:
            file_path = os.path.join(root, file)

            # Lecture du contenu chiffré
            with open(file_path, "rb") as f:
                encrypted_data = f.read()

            try:
                # Tentative de déchiffrement
                decrypted_data = fernet.decrypt(encrypted_data)

                # Restitution de la donnée en texte clair
                with open(file_path, "wb") as f:
                    f.write(decrypted_data)

                print(f"[🔓 DECHIFFREMENT] Fichier restauré : {file_path}")
            except Exception:
                print(
                    f"[❌ ERREUR] Échec du déchiffrement pour : {file_path}. "
                    "Clé invalide."
                )

    print("\n" + "=" * 60)
    print(" [✅] Opération Al-Basit terminée avec succès. ")
    print(" Vérifie à nouveau le contenu de ton dossier 'vault_documents'.")
    print("=" * 60)


if __name__ == "__main__":
    execute_decryption()
    
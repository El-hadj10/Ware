#!/bin/bash

# =========================================================================
# SETUP.SH - INITIALISATION SECURISEE DU LABO WARE (UBUNTU)
# =========================================================================

set -e # Interrompt le script en cas d'erreur

echo -e "\e[1;34m[*] Initialisation de l'environnement virtuel pour Ware...\e[0m"

# 1. Vérification et installation des prérequis système
if ! command -v python3 &> /dev/null; then
    echo -e "\e[1;31m[-] Erreur: Python3 n'est pas installé sur ce système.\e[0m"
    exit 1
fi

# 2. Création de l'environnement virtuel local
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "\e[1;32m[+] Environnement virtuel 'venv' créé avec succès.\e[0m"
else
    echo -e "\e[1;33m[!] Un environnement 'venv' existe déjà. Passage à l'étape suivante.\e[0m"
fi

# 3. Activation de l'environnement virtuel et mise à jour de pip
source venv/bin/activate
echo -e "\e[1;34m[*] Mise à jour de l'installeur pip...\e[0m"
pip install --upgrade pip

# 4. Installation des dépendances centralisées
if [ -f "requirements.txt" ]; then
    echo -e "\e[1;34m[*] Installation des dépendances depuis requirements.txt...\e[0m"
    pip install -r requirements.txt
    echo -e "\e[1;32m[+] Toutes les dépendances logicielles ont été installées.\e[0m"
else
    echo -e "\e[1;31m[-] Erreur critique: requirements.txt introuvable à la racine.\e[0m"
    exit 1
fi

echo -e "\e[1;32m[+] [CONFIGURATION TERMINEE] Pour activer le laboratoire, exécutez :\e[0m"
echo -e "\e[1;35m    source venv/bin/activate\e[0m"
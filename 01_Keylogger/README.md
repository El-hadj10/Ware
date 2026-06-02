# Étape 01 : Keylogger (Enregistreur de frappe)

Ce module étudie les mécanismes d'interception des flux d'entrées (I/O) sous Linux Ubuntu, ainsi que l'impact de l'analyse automatisée par IA.

## 📝 Concepts Clés
* **Méthode :** Capture via les API du serveur d'affichage (X11) ou lecture directe de `/dev/input/`.
* **Évolution IA :** Filtrage sémantique en temps réel (extraction automatique des structures de mots de passe, cartes bancaires, etc.).
* **Intention & Protection :** *Al-Hafiz* (Le Préservateur). Comprendre pour préserver l'intégrité de nos accès secrets.

## 🛠️ Dépendances (Ubuntu)
Avant de lancer le script, l'environnement nécessite l'installation de certains paquets système et de la bibliothèque Python de capture.

```bash
sudo apt update
sudo apt install python3-pip python3-dev
pip3 install pynput

## 🚀 Exécution du PoC
Pour lancer le script de démonstration :
```bash
python3 keylogger_poc.py
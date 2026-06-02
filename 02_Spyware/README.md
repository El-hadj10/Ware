# Étape 02 : Spyware / Infostealer

Ce module étudie les mécanismes d'exploration active, de ciblage et de centralisation de données sensibles (secrets, configurations, sessions) au sein d'un environnement Linux Ubuntu.

---

## 📋 Navigation Rapide
* 🔙 [Retour à la Feuille de Route Globale](../ROADMAP.md)
* 📄 [Accéder au Script du Laboratoire](./infostealer_poc.py)
* 📂 [Voir la Zone de Centralisation (Dropzone)](./exfil_dropzone) *(Générée après exécution)*

---

## 📝 Concept Technique
Contrairement à une écoute passive comme le Keylogger, l'Infostealer agit par scans ciblés, récursifs et opportunistes. Il exploite les variables d'environnement et les chemins de fichiers standards pour extraire des secrets d'authentification avant qu'ils ne soient chiffrés ou transmis.

### Évolution avec l'Intelligence Artificielle
Les versions traditionnelles cherchaient des noms de fichiers figés. Les variantes modernes intègrent des expressions régulières intelligentes et des modèles NLP (Natural Language Processing) locaux capables de lire le *contenu sémantique* des fichiers texte bruts. Une IA offensive peut ainsi détecter instantanément une clé d'API, une seed-phrase de crypto-monnaie ou un mot de passe, même si le fichier est nommé de manière anodine.

---

## 🔐 Intention & Protection
* **Invocation 99 :** *Al-Basir* (Le Clairvoyant / Celui qui voit l'invisible).
* **Objectif :** Développer la clairvoyance technique pour identifier les fichiers laissés vulnérables sur nos configurations afin de préserver l'invisible de nos accès secrets.

---

## 🛠️ Protocole d'Exécution du Laboratoire

Le script utilise exclusivement les bibliothèques standards de Python 3 (`os`, `shutil`, `json`, `datetime`) pour simuler une empreinte minimale sans dépendances tierces. Il génère automatiquement un faux profil utilisateur (`fake_user_profile`) pour effectuer ses tests en toute sécurité.

### 1. Donner les droits d'exécution au script
```bash
chmod +x infostealer_poc.py


./infostealer_poc.py

============================================================
[🔍 DECOUVERTE] Fichier sensible identifié : ./fake_user_profile/notes_crypto.txt
[🔍 DECOUVERTE] Fichier sensible identifié : ./fake_user_profile/.ssh/id_rsa
[🔍 DECOUVERTE] Fichier sensible identifié : ./fake_user_profile/config/.env

============================================================
 [✅] Analyse terminée. 3 fichiers centralisés.
 Consultez le dossier './exfil_dropzone' pour analyser les données collectées.
============================================================

🛡️ Analyse des Contre-mesures & Détection
L'analyse du fichier de rapport exfil_manifest.json après exécution met en évidence les failles typiques d'un système. Pour s'en prémunir :

Chiffrement des clés au repos : Ne jamais laisser de clés SSH privées sans passphrase. Une clé chiffrée nécessite une saisie utilisateur et devient inutile pour un Infostealer automatisé.

Gestion des Variables d'Environnement : Éviter de stocker des fichiers .env en texte brut dans les dossiers de projets de manière prolongée. Utiliser des gestionnaires de secrets professionnels (comme Vault, Doppler ou le trousseau sécurisé d'Ubuntu).

Contrôle d'Accès Réseau (Egress Filtering) : Un stealer doit impérativement envoyer son manifeste JSON et ses captures vers un serveur externe (C2). Un pare-feu configuré pour bloquer les flux sortants non autorisés neutralise l'impact de l'attaque.
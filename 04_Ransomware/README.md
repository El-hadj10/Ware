# Étape 04 : Ransomware (PoC Cryptographique)

Ce module explore les fondements mathématiques et comportementaux du chiffrement au repos, de la séquestration de fichiers et des protocoles de restauration.

---

## 📋 Navigation Rapide
* 🔙 [Retour à la Feuille de Route Globale](../ROADMAP.md)
* 🔐 [Accéder au Script de Chiffrement (Al-Qabid)](./ransomware_encrypt.py)
* 🔓 [Accéder au Script de Déchiffrement (Al-Basit)](./ransomware_decrypt.py)
* 📂 [Explorer les Documents Cibles](./vault_documents) *(Générés après exécution)*

---

## 📝 Concept Technique
Un ransomware moderne est un agent de manipulation cryptographique asymétrique ou symétrique à haute performance. Contrairement à une attaque destructrice classique (comme un `rm -rf`), il préserve l'intégrité physique de la donnée tout en révoquant son accès sémantique.

### Évolution avec l'Intelligence Artificielle
Les vagues de ransomwares traditionnels appliquaient un chiffrement uniforme et massif, générant des pics d'I/O (opérations d'écriture sur le disque) et de CPU instantanément interceptés par les règles heuristiques des EDR (Endpoint Detection and Response).

L'intégration de l'IA permet l'émergence du **chiffrement intermittent et adaptatif** :
* Le flux d'altération imite sémantiquement les opérations de logiciels légitimes (outils d'indexation, compression, processus de mise à jour système d'Ubuntu).
* Des algorithmes de tri prédictif analysent la valeur et la criticité des données découvertes en temps réel afin d'ajuster le montant de la rançon demandé de manière chirurgicale.

---

## 🔐 Intention & Protection
* **Dynamic Spirituelle :** * *Al-Qabid* (Celui qui restreint / Phase de verrouillage).
  * *Al-Basit* (Celui qui déploie / Phase de libération et restauration).
* **Objectif :** Comprendre qu'un accès numérique n'est jamais acquis. Seule l'architecture d'une résilience immuable (sauvegardes hors-ligne, déconnectées du réseau) garantit la libération d'une infrastructure face à une restriction forcée.

---

## 🛠️ Protocole d'Exécution du Laboratoire

Pour manipuler ce module en toute sécurité sans impacter tes fichiers de configuration Ubuntu, nous allons utiliser la bibliothèque standard `cryptography` au sein de notre environnement isolé.

## 1. Installation de la dépendance de chiffrement
Assure-toi que ton `(venv)` est actif dans ton terminal et installe le module requis :
```bash
pip install cryptography

## 2. Exécution des PoC
Générer les documents et simuler le chiffrement (Al-Qabid) :
```bash
python3 ransomware_encrypt.py

Appliquer la clé de restauration pour libérer les fichiers (Al-Basit) :
```bash
python3 ransomware_decrypt.py

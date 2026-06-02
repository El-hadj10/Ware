# Dossier "Ware" - Feuille de Route & Laboratoire d'Analyse

Ce dossier regroupe les travaux d'étude, d'analyse et de développement de *Proofs of Concept* (PoC) concernant les différentes catégories de codes malveillants et de programmes d'infrastructure. L'objectif est de comprendre les mécanismes cyberoffensifs modernes à l'ère de l'Intelligence Artificielle pour mieux structurer la cyberdéfense.

---

## 📋 Tableau de Bord & Feuille de Route Cliquable

*Cliquez sur le nom du sujet pour accéder directement à son espace de laboratoire et sa documentation spécifique.*

| Étape | Sujet Principal | Focus Technique | Invocation 99 & Intention | Transliteration | Invocation en arabe | Status |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| **01** | [📁 Keylogger](./01_Keylogger) | Capture d'entrées, gestion des flux (I/O) | *Al-Hafiz* (Le Préservateur / Protéger l'accès) | Yâ Hafîz | يَا حَفِيظُ | ✅ Terminé |
| **02** | [📁 Spyware / Stealer](./02_Spyware) | Exfiltration de données, persistance légère | *Al-Basir* (Le Clairvoyant / Détecter l'invisible) | Yâ Basîr | يَا بَصِيرُ | ✅ Terminé |
| **03** | [📁 Worm (Ver)](./03_Worm) | Auto-réplication, scan de réseau local | *Al-Muhsi* (Celui qui prend compte / Propagation) | Yâ Muhsî | يَا مُحْصِي | ⏳ En cours |
| **04** | [📁 Ransomware](#) | Chiffrement de fichiers (Crypto), gestion des clés | *Al-Qabid / Al-Basit* (Celui qui restreint / libère) | Yâ Qâbid / Yâ Bâsit | يَا قَابِضُ / يَا بَاسِطُ | ⏳ En attente |
| **05** | [📁 Malware IA (Moderne)](#) | Obfuscation dynamique, contournement d'EDR | *Al-Latif* (Le Subtil / Analyse des menaces fines) | Yâ Latîf | يَا لَطِيفُ | ⏳ En attente |

---

## 🛠️ Protocole d'Étude (Par Sujet)

Pour chaque module de cette feuille de route, nous suivrons un processus d'ingénierie rigoureux avant de passer au sujet suivant :
1. **Analyse Théorique :** Compréhension fine des vecteurs d'attaque, des API système exploitées et de l'impact des technologies IA sur la menace.
2. **Développement du Script (PoC) :** Écriture d'un code minimaliste, commenté et confiné, visant à observer le comportement technique exact au sein du laboratoire.
3. **Documentation & Contre-mesures :** Identification des indicateurs de compromission (IoC), méthodes de détection heuristique/comportementale et stratégies de remédiation.

## ⚠️ Consignes de Sécurité du Laboratoire
* Toutes les manipulations et exécutions de scripts doivent impérativement être effectuées au sein d'un environnement virtualisé, isolé du réseau principal (Sandbox, Machine Virtuelle dédiée de type Kali Linux / Ubuntu ou conteneur hermétique).
* Les codes produits ont une visée exclusivement éducative et de recherche en sécurité informatique.
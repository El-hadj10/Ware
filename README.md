# 📘 ARCHITECTURE DES LOGICIELS MALVEILLANTS : DE LA CONCEPTION À LA DÉTECTION
> **Un traité d'ingénierie système, d'analyse comportementale et de cyberdéfense moderne.**

---

## 📊 TABLEAU DE BORD DU LABORATOIRE

![Plateforme Linux](https://img.shields.io/badge/Platform-Linux%20Ubuntu-orange?style=for-the-badge&logo=ubuntu)
![Langage Python](https://img.shields.io/badge/Language-Python%203.12-blue?style=for-the-badge&logo=python)
![Statut du Projet](https://img.shields.io/badge/Status-100%25%20Termin%C3%A9-brightgreen?style=for-the-badge)

*Cliquez sur les modules ci-dessous pour accéder directement aux répertoires de code et documentations spécifiques du laboratoire.*

| Module | Sujet Principal | Focus Système | Vecteur d'Action | Alignement Spirituel | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **01** | [📁 Keylogger (Enregistreur)](./01_Keylogger) | Interception des interruptions d'E/S | Écoute passive de flux | *Al-Hafiz* (Le Préservateur) | ![Terminé](https://img.shields.io/badge/%E2%9C%85-Termin%C3%A9-green) |
| **02** | [📁 Spyware / Infostealer](./02_Spyware) | Exploration récursive de fichiers | Exfiltration de secrets | *Al-Basir* (Le Clairvoyant) | ![Terminé](https://img.shields.io/badge/%E2%9C%85-Termin%C3%A9-green) |
| **03** | [📁 Worm (Ver Informatique)](./03_Worm) | Topologie & Protocoles Réseau | Propagation autonome | *Al-Muhsi* (Le Comptabilisateur) | ![Terminé](https://img.shields.io/badge/%E2%9C%85-Termin%C3%A9-green) |
| **04** | [📁 Ransomware (Rançongiciel)](./04_Ransomware) | Primitives Cryptographiques | Chiffrement symétrique | *Al-Qabid / Al-Basit* | ![Terminé](https://img.shields.io/badge/%E2%9C%85-Termin%C3%A9-green) |
| **05** | [📁 Malware IA / Polymorphe](./05_Malware_IA) | Algorithmes d'Obfuscation | Mutation structurelle | *Al-Latif* (Le Subtil) | ![Terminé](https://img.shields.io/badge/%E2%9C%85-Termin%C3%A9-green) |

---

## 📖 LIVRE TECHNIQUE : LE COMPENDIUM DES MENACES SYSTEME

---

### 📑 CHAPITRE 1 : LE KEYLOGGER (L'INTERCEPTION DES FLUX D'ENTRÉE)

#### 1. Nature et Propriétés
Le Keylogger (enregistreur de frappes) est un outil de reconnaissance et d'espionnage dont le but premier est la captation exhaustive de l'activité clavier de l'utilisateur. Sa nature intrinsèque exige une discrétion absolue : il doit consommer un minimum de ressources CPU et s'interposer de façon transparente entre le périphérique matériel (clavier) et le serveur d'affichage graphique (X11 ou Wayland sous Ubuntu).

#### 2. Conception et Mécanismes
La conception d'un Keylogger sous Linux repose sur la capture des flux d'événements d'E/S (Entrées/Sorties). Au niveau du noyau, chaque pression sur une touche génère une interruption matérielle traduite en `scancode`. Le keylogger intercepte ces signaux soit :
* En lisant directement les fichiers de périphériques dans `/dev/input/event*` (nécessite des privilèges root).
* En s'abonnant aux hooks globaux du serveur d'affichage via des bibliothèques de haut niveau telles que `pynput` ou `Xlib`.

Le script capture le flux séquentiel des caractères, mappe les codes de touches spéciales (comme `Shift`, `Space`, `Enter`) et écrit ces données de manière ordonnée dans un fichier tampon persistant.

#### 3. Déploiement et Agissement
Le déploiement s'effectue généralement par le biais de scripts d'automatisation ou d'ingénierie sociale (paquet contrefait). Une fois exécuté, le Keylogger installe un thread d'écoute en arrière-plan (Background Worker) qui surveille en permanence la file d'attente des événements du système. Il reste dormant tant qu'aucune touche n'est pressée, évitant ainsi de saturer les moniteurs d'activité.

#### 4. Exploitation et Cyberdéfense
Les données accumulées permettent d'isoler des informations critiques par analyse sémantique textuelle : identifiants de connexion, coordonnées bancaires, ou correspondances privées. 
* **Détection :** Surveillance des descripteurs de fichiers ouverts sur `/dev/input/`, détection de comportements anomaux via l'audit des hooks du serveur graphique.
* **Remédiation :** Utilisation du serveur d'affichage Wayland (mieux cloisonné que X11), implémentation de claviers virtuels avec disposition aléatoire des touches pour brouiller l'interception des scancodes.

---

### 📑 CHAPITRE 2 : L'INFOSTEALER (LE PILLEUR DE SECRETS SÉMANTIQUES)

#### 1. Nature et Propriétés
L'Infostealer (voleur d'informations) est un agent offensif hautement ciblé et opportuniste. Contrairement à un Keylogger qui attend passivement les actions futures, l'Infostealer réalise un raid instantané sur les données existantes accumulées au repos sur le disque dur. Il recherche en priorité des données à haute valeur financière ou stratégique.

#### 2. Conception et Mécanismes
La conception d'un stealer s'appuie sur la prévisibilité des systèmes de fichiers d'exploitation. Les développeurs de logiciels (navigateurs, clients SSH, portefeuilles applicatifs) stockent les configurations dans des répertoires standards. Le stealer implémente un algorithme de parcours récursif de l'arborescence (arbre de répertoires comme `os.walk`) combiné à un filtrage heuristique basé sur des expressions régulières ou des mots-clés sémantiques (`.env`, `id_rsa`, `crypto`, `wallet`).

#### 3. Déploiement et Agissement
Introduit souvent par le biais de chaînes d'approvisionnement corrompues (Supply Chain Attack) ou de dépendances malveillantes, l'Infostealer s'exécute en une fraction de seconde. Il scanne le répertoire de l'utilisateur actuel (`~/*`), copie les fichiers identifiés comme sensibles dans un espace de transit temporaire appelé "Dropzone", puis structure un manifeste global au format JSON contenant les métadonnées de la collecte.

#### 4. Exploitation et Cyberdéfense
Les fichiers centralisés dans la dropzone sont compressés et exfiltrés vers un serveur de Command & Control (C2) externe par des requêtes HTTP/HTTPS ou DNS. L'attaquant obtient immédiatement des clés d'API, des cookies de session permettant de contourner la double authentification (2FA), et des accès SSH à des serveurs distants.
* **Détection :** Détection de scans de fichiers intensifs non initiés par l'utilisateur, surveillance des connexions réseau sortantes inhabituelles vers des adresses IP inconnues (Egress Filtering).
* **Remédiation :** Chiffrement obligatoire des clés privées à l'aide d'une phrase de passe robuste, utilisation de gestionnaires de secrets centralisés et sécurisés au lieu de fichiers texte `.env` bruts.

---

### 📑 CHAPITRE 3 : LE WORM (L'AUTONOMIE DU MOUVEMENT LATÉRAL)

#### 1. Nature et Propriétés
Le Ver informatique (Worm) se caractérise par son **autonomie absolue** et sa capacité d'auto-réplication. Alors qu'un virus classique nécessite un hôte (un fichier à infecter) et une intervention humaine pour se propager, le ver exploite l'infrastructure réseau pour naviguer de machine en machine, étendant son rayon d'action de façon géométrique.

#### 2. Conception et Mécanismes
Un ver est conçu autour de trois composants logiciels fondamentaux :
1. **Le module de reconnaissance (Scanner) :** Analyse les interfaces réseau locales, détermine la plage d'adresses IP (ex: `192.168.1.0/24`) et effectue des balayages de ports (port scanning) pour repérer des services réseau actifs (ex: SSH sur le port 22, SMB sur le port 445).
2. **Le module d'exploitation (Payload Launcher) :** Exploite une faille de sécurité logicielle ou teste des listes d'identifiants par force brute (Credential Stuffing).
3. **Le module de réplication :** Utilise des fonctions de transfert de fichiers (`shutil.copy`, protocoles de transfert réseau) pour injecter son propre code source exact sur la machine distante et l'activer.

#### 3. Déploiement et Agissement
Dès qu'un nœud initial est compromis, le ver prend vie de manière indépendante. Il cartographie son nouveau sous-réseau, énumère les voisins disponibles, implémente des mécanismes d'idempotence (vérification de la présence d'un fichier indicateur de statut pour ne pas sur-infecter une cible déjà compromise), puis se duplique à la volée vers les cibles valides.

#### 4. Exploitation et Cyberdéfense
L'exploitation réseau par un ver peut saturer la bande passante d'une entreprise en quelques minutes et paralyser l'infrastructure globale par déni de service (DoS) ou par infection généralisée.
* **Détection :** Identification de pics anormaux de scans de ports internes, alertes de pare-feu sur des connexions latérales inhabituelles entre postes de travail.
* **Remédiation :** Micro-segmentation stricte des réseaux (isoler la comptabilité du secrétariat ou du développement), désactivation des protocoles d'administration à distance non sécurisés, et application immédiate des correctifs de sécurité système (Patch Management).

---

### 📑 CHAPITRE 4 : LE RANSOMWARE (LA SÉQUESTRATION CRYPTOGRAPHIQUE)

#### 1. Nature et Propriétés
Le Ransomware (rançongiciel) est un code malveillant d'extorsion financière. Sa nature est purement asymétrique : il n'altère pas l'infrastructure physique du système et ne détruit pas les fichiers au sens classique (pas d'effacement). Il révoque l'accès logique et sémantique aux données de la victime en modifiant leur état à l'aide d'algorithmes cryptographiques de niveau militaire.

#### 2. Conception et Mécanismes
La conception d'un ransomware moderne repose sur un système de chiffrement hybride pour optimiser les performances :
* **Chiffrement Symétrique (Phase Al-Qabid) :** Le malware énumère les volumes de stockage et chiffre le contenu des fichiers utilisateur à très haute vitesse à l'aide d'une clé symétrique unique (AES ou algorithme Fernet basé sur des blocs de clés de 128/256 bits). Le texte brut est transformé en un bloc binaire obfusqué (commençant par exemple par `gAAAAAB...`).
* **Chiffrement Asymétrique :** La clé symétrique utilisée pour chiffrer les fichiers est ensuite elle-même chiffrée avec une clé publique asymétrique (RSA/ECC) appartenant à l'attaquant. La clé privée nécessaire pour inverser l'opération n'est jamais présente sur la machine de la victime.

#### 3. Déploiement et Agissement
Le ransomware cible spécifiquement les extensions de documents critiques (`.docx`, `.xlsx`, `.pdf`, `.db`) tout en évitant minutieusement les fichiers vitaux du système d'exploitation (`/boot`, `/usr/lib`) afin de maintenir la machine opérationnelle pour l'affichage de la note de rançon. Une fois le chiffrement achevé, il supprime les clichés instantanés (shadow copies), vide les caches et dépose des instructions de paiement.

#### 4. Exploitation et Cyberdéfense
Sans la clé privée détenue par l'attaquant, le déchiffrement de la structure est mathématiquement impossible en temps humain. La restauration ne peut s'opérer que par l'injection de la clé légitime (Phase *Al-Basit*).
* **Détection :** Surveillance des taux de modification de fichiers extrêmement élevés par seconde (pics d'I/O), détection des modifications d'extensions massives via des règles de comportement.
* **Remédiation :** Implémentation d'une stratégie de sauvegarde immuable 3-2-1 (trois copies, deux supports différents, une copie hors-ligne isolée physiquement du réseau), déploiement de fichiers "canaris" (Honeytokens) pour piéger le processus de chiffrement dès son amorce.

---

### 📑 CHAPITRE 5 : LE MALWARE IA & POLYMOPHE (L'OBFUSCATION ET L'MUTATION SUBTILE)

#### 1. Nature et Propriétés
Le Malware IA ou Polymorphe représente le sommet de l'évolution des menaces numériques adaptatives. Sa propriété principale est la **fluidité structurelle**. Contrairement à tous les codes précédents qui conservent une forme logicielle identique au fil de leurs exécutions, le malware polymorphe modifie son apparence et sa composition syntaxique en permanence, tout en préservant ses capacités fonctionnelles initiales.

#### 2. Conception et Mécanismes
Un moteur de polymorphisme s'appuie sur la génération de code dynamique. À chaque cycle ou réplication, l'orchestrateur exécute un algorithme de mutation automatique :
* **Génération de variables aléatoires :** Les noms des fonctions, des classes et des variables internes sont remplacés par des chaînes de caractères chaotiques générées à la volée.
* **Injection de Junk Data (Dead Code) :** Des lignes de commentaires aléatoires et des opérations mathématiques inutiles sont insérées pour modifier la taille et l'agencement du fichier.
* **Chiffrement / Encodage variable :** La charge utile principale est encodée de manière itérative (ex: Base64 dynamique) et enveloppée dans une fonction de décodage unique (mécanisme `exec()`).

Ce processus garantit que **l'empreinte cryptographique (le hash SHA-256) du fichier change à chaque seconde**, neutralisant instantanément la détection par signature.

#### 3. Déploiement et Agissement
Idéal pour les opérations d'espionnage persistant (APT), ce type de malware agit avec une extrême subtilité. Il intègre des modules logiques d'auto-analyse environnementale. S'il détecte des indices révélant la présence d'outils de surveillance, de débogueurs ou de bacs à sable (Sandbox/VM), il s'abstient de toute action suspecte, s'endort, ou simule le comportement d'une application légitime (ex: une calculatrice ou un composant système).

#### 4. Exploitation et Cyberdéfense
L'exploitation réussie d'un code polymorphe lui permet de séjourner des mois ou des années au sein d'une infrastructure d'entreprise sans jamais déclencher les alertes des solutions antivirus traditionnelles basées sur des listes de blocage.
* **Détection :** Abandon complet de l'analyse statique au profit de l'**Analyse Comportementale Avancée (EDR/XDR)**. Surveillance des hooks système en mémoire vive (AMSI / Script Control) au moment précis où le code se déballe pour s'exécuter.
* **Remédiation :** Intégration de modèles d'apprentissage automatique locaux au sein des agents de sécurité pour détecter les structures logiques d'obfuscation et de dépaquetage dynamique en temps réel.

---

## 🛠️ CONSIGNES DE SÉCURITÉ DE L'INGÉNIEUR

L'intégralité des codes sources développés au sein de ce projet sont des *Proofs of Concept* (PoC) confinés, configurés pour s'exécuter au sein d'environnements virtuels isolés (`venv`) ou de bacs à sable simulés localement. 

Leur utilisation est strictement réservée à l'étude des mécanismes de défense, à l'analyse heuristique et à la recherche académique en sécurité informatique. **La sécurité d'une infrastructure commence par la compréhension fine de sa vulnérabilité.**
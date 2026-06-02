# Étape 03 : Worm (Ver informatique)

Ce module étudie les mécanismes de reconnaissance réseau, de balayage de ports (scanning) et de réplication autonome (mouvements latéraux) au sein d'une infrastructure confinée.

---

## 📋 Navigation Rapide
* 🔙 [Retour à la Feuille de Route Globale](../ROADMAP.md)
* 📄 [Accéder au Script du Laboratoire](./worm_poc.py)
* 📂 [Explorer le Réseau Virtuel Cible](./virtual_network) *(Généré après exécution)*

---

## 📝 Concept Technique
Un ver informatique (Worm) se distingue des autres codes malveillants par son autonomie complète. Il n'a pas besoin de s'attacher à un programme existant ni d'une action humaine pour se propager. 

Sa cinématique repose sur un cycle itératif :
1. **Reconnaissance :** Découverte des adresses IP actives sur le segment réseau.
2. **Scan de ports :** Identification des services vulnérables ou exploitables (ex: SSH, SMB).
3. **Mouvement Latéral :** Auto-copie et exécution distante sur la nouvelle cible.

### Évolution avec l'Intelligence Artificielle
Les vers traditionnels effectuent des balayages séquentiels ou aléatoires extrêmement massifs, ce qui déclenche immédiatement les alertes des pare-feu et des systèmes de détection d'intrusion (IDS). 
Les vers modernes basés sur l'IA utilisent l'apprentissage par renforcement pour analyser passivement le trafic réseau légitime. Ils apprennent la topologie de l'entreprise sans faire de bruit, imitent les flux de travail humains et sélectionnent intelligemment le **chemin de propagation optimal** (en ciblant en priorité les machines critiques ou mal surveillées) pour contourner les centres de surveillance (SOC).

---

## 🔐 Intention & Protection
* **Invocation 99 :** *Al-Muhsi* (Celui qui prend compte / Le Comptabilisateur).
* **Objectif :** Maîtriser la cartographie complète de notre infrastructure. Pour bloquer un ver, il faut être capable de dénombrer et d'auditer chaque équipement connecté afin de ne laisser aucune zone d'ombre vulnérable.

---

## 🛠️ Protocole d'Exécution du Laboratoire

Pour des raisons de sécurité évidentes, ce PoC est **100% confiné dans un réseau virtuel simulé en local** sous forme de dossiers. Il ne génère aucun trafic réseau réel sur ton Ubuntu et ne sortira jamais de ta machine.

### 1. Donner les droits d'exécution au script
```bash
chmod +x worm_poc.py
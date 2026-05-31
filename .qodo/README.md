# 📦 Dossier `.qodo/` — Orchestration GoDo & Automatisation Sécurité

![MIT License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Qodo Agents](https://img.shields.io/badge/Agents%20Qodo-100%25%20valid%C3%A9s-brightgreen?style=flat-square)
![Pre-commit Hook](https://img.shields.io/badge/Pre--commit%20Hook-activ%C3%A9-blue?style=flat-square)

Ce dossier centralise toute la logique d’automatisation, d’audit et de workflows pour le laboratoire Ware, en lien avec l’extension GoDo.

## Structure

- `agents/` : Agents pentest (un par module, format godo_agent.json)
- `workflows/` : Scripts d’orchestration, automatisations, rapports
- `reports/` : (optionnel) Archives des audits et rapports générés


## Utilisation

- **Dashboard d’intégrité** :
  - Lance `.qodo/workflows/qodo_resonance.py` pour afficher la jauge d’intégrité globale, la bannière ASCII, et la progression de chaque agent (statuts : À faire, En cours, Terminé).
  - Affichage harmonieux, synthèse visuelle, et messages d’honneur si un module est complété.

- **Orchestrateur** :
  - Lance `.qodo/workflows/godo_orchestrator.py` pour explorer, afficher et simuler les audits sécurité de chaque module.
  - Les agents sont découverts automatiquement dans `.qodo/agents/`.

- **Ajout d’un agent** :
  - Crée un dossier au nom du module dans `.qodo/agents/`.
  - Ajoute un fichier `godo_agent.json` avec la structure standard (voir exemples existants).
  - Chaque agent doit comporter des tâches avec les statuts : "À faire", "En cours", "Terminé" pour un suivi optimal.

- **Automatisation** :
  - Place ici tous les scripts Python, YAML ou autres liés à la gestion des tâches, audits, CI/CD, etc.

## Validation et Qualité

- **flake8** :
  - Tous les scripts de `.qodo/workflows/` sont validés flake8 (aucune erreur tolérée).
  - Le hook pre-commit bloque tout commit non conforme.

- **Validation agents** :
  - `.qodo/workflows/validate_agents.py` vérifie la structure et la complétude de chaque agent.

## Tests

- Pour tester le dashboard d’intégrité :
  ```bash
  python3 .qodo/workflows/qodo_resonance.py
  ```
- Pour simuler un audit complet :
  ```bash
  python3 .qodo/workflows/godo_orchestrator.py
  ```

## Philosophie

L’Ordre, la Lumière et la Clarté guident la structure Qodo. Chaque agent, chaque jauge, chaque badge reflète la progression et la rigueur du laboratoire Ware.


## Installation du hook pre-commit

Après un clonage du dépôt, lance :

```bash
python3 .qodo/workflows/install_hooks.py
```

Ceci installe un hook qui bloque tout commit si flake8 ou la validation Qodo échoue.

---

## Exemples

- Pour lancer l’orchestrateur :
  ```bash
  cd .qodo/workflows
  python godo_orchestrator.py
  ```

- Pour ajouter un rapport d’audit :
  ```bash
  mkdir -p .qodo/reports
  # Générer un rapport Markdown ou HTML ici
  ```

## Bonnes pratiques

- Ne jamais placer de scripts GoDo à la racine du projet.
- Versionner `.qodo/` (hors secrets) pour garder l’historique des audits.
- Documenter chaque agent et workflow pour faciliter la maintenance.

---

> Dépôt GitHub : https://github.com/El-hadj10/Ware
> Auteur : El-hadj Nour

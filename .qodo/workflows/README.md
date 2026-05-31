# 📜 Workflows & Automatisations GoDo

![MIT License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Qodo Orchestrator](https://img.shields.io/badge/Orchestrateur-Op%C3%A9rationnel-brightgreen?style=flat-square)
![Pre-commit Hook](https://img.shields.io/badge/Pre--commit%20Hook-activ%C3%A9-blue?style=flat-square)

Ce dossier contient tous les scripts d’orchestration, de validation et d’automatisation liés à la gestion des agents GoDo pour le laboratoire Ware.


## Scripts présents

- `qodo_resonance.py` : Dashboard d’intégrité, jauge globale, bannière ASCII, synthèse des agents et progression visuelle.
- `godo_orchestrator.py` : Orchestrateur centralisé pour explorer, afficher et simuler les audits sécurité de chaque module.
- `validate_agents.py` : Vérifie la validité et la structure de tous les fichiers `godo_agent.json`.

## Qualité et conformité

- Tous les scripts sont validés flake8 (aucune erreur tolérée).
- Le hook pre-commit bloque tout commit non conforme.

## Philosophie

Chaque workflow vise la clarté, la robustesse et l’automatisation harmonieuse du laboratoire Ware.


## Installation du hook pre-commit

Après un clonage du dépôt, lance :

```bash
python3 install_hooks.py
```

Ceci installe un hook qui bloque tout commit si flake8 ou la validation Qodo échoue.

---

## Utilisation

```bash
cd .qodo/workflows
python godo_orchestrator.py
python validate_agents.py
```

Ajoute ici tous tes futurs workflows ou automatisations liés à GoDo.

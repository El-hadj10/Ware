# À PROPOS DU DOSSIER `.qodo/`

![MIT License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Qodo Agents](https://img.shields.io/badge/Agents%20Qodo-100%25%20valid%C3%A9s-brightgreen?style=flat-square)
![Pre-commit Hook](https://img.shields.io/badge/Pre--commit%20Hook-activ%C3%A9-blue?style=flat-square)

Ce dossier est le cœur de l’automatisation, de l’audit et de la gouvernance technique du laboratoire Ware.

## Objectif

Centraliser tous les agents, workflows, rapports et scripts liés à la sécurité, à la conformité et à la qualité logicielle, en s’appuyant sur l’extension GoDo pour VS Code.

## Contenu
- `agents/` : Un agent pentest par module, chacun avec ses tâches d’audit.
- `workflows/` : Orchestrateur, validateurs, automatisations.
- `reports/` : Rapports d’audit générés ou archivés.
- `TODO.md` : Suivi des améliorations et automatisations à venir.


## Philosophie

- **Clarté** : Chaque action d’audit ou de workflow est documentée et traçable.
- **Ordre** : Aucun script GoDo ne doit sortir de `.qodo/`.
- **Évolutivité** : La structure permet d’ajouter facilement de nouveaux modules, agents ou automatisations.
- **Intégrité** : Le dashboard d’intégrité (`qodo_resonance.py`) synthétise la progression et la santé du laboratoire.
- **Qualité** : Tous les workflows sont validés flake8 et soumis à un contrôle automatique à chaque commit.

## Vision d’ensemble

Le dossier `.qodo/` incarne la gouvernance technique : automatisation, audit, documentation et traçabilité réunies pour garantir la robustesse et la transparence du projet Ware.

## Auteur
El-hadj Nour — https://github.com/El-hadj10/Ware

---

*Ce dossier est versionné pour garantir la transparence, la reproductibilité et la sécurité des processus d’audit du projet Ware.*

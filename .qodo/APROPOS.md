# À PROPOS DU DOSSIER `.qodo/`

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

## Auteur
El-hadj Nour — https://github.com/El-hadj10/Ware

---

*Ce dossier est versionné pour garantir la transparence, la reproductibilité et la sécurité des processus d’audit du projet Ware.*

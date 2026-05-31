# Agents GoDo — Laboratoire Ware

![MIT License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Agents Qodo](https://img.shields.io/badge/Agents%20Qodo-100%25%20valid%C3%A9s-brightgreen?style=flat-square)

Ce dossier contient un agent pentest par module du projet Ware, chacun sous la forme d’un fichier `godo_agent.json`.

## Convention
- Un sous-dossier par module (ex : Keylogger, Spyware, Worm, ...)
- Un fichier `godo_agent.json` par agent

## Exemple de structure

```
.qodo/agents/
  Keylogger/
    godo_agent.json
  Spyware/
    godo_agent.json
  Worm/
    godo_agent.json
  ...
```


## Format minimal d’un agent

```json
{
  "name": "Audit sécurité Worm",
  "description": "Agent pentest chargé de vérifier la sécurité du module Worm.",
  "type": "pentest",
  "module": "03_Worm",
  "tasks": [
    { "title": "Analyse des mécanismes de propagation", "status": "À faire" }
  ]
}
```

## Statuts des tâches

Chaque tâche d’agent doit avoir un statut parmi :
- `À faire` — tâche à réaliser
- `En cours` — tâche en cours d’audit
- `Terminé` — tâche validée

Cela permet au dashboard d’intégrité d’afficher la progression réelle de chaque module.

## Validation automatique

Le script `.qodo/workflows/validate_agents.py` vérifie la structure et la complétude de chaque agent à chaque commit (hook pre-commit).

## Philosophie

Chaque agent est un gardien de l’Ordre : clarté, granularité, traçabilité.

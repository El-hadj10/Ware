# 06 — Backdoor C2 (Command & Control)

> **Module Red Team** · Simulation d'un canal C2 reverse shell

---

## Description

Simule un agent malveillant qui établit une connexion TCP persistante
vers un contrôleur C2 sur `127.0.0.1:4444`.  
Le contrôleur peut envoyer des commandes shell arbitraires ; l'agent
les exécute et renvoie la sortie, avec reconnexion automatique.

---

## Fichiers

| Fichier | Rôle |
|---|---|
| `backdoor_c2_poc.py` | Agent C2 + contrôleur interactif |

---

## Usage

```bash
# Terminal 1 — Contrôleur (écoute sur 4444)
python3 backdoor_c2_poc.py controller

# Terminal 2 — Agent (reverse shell)
python3 backdoor_c2_poc.py
```

---

## Comportements simulés

- Connexion TCP sortante persistante vers `127.0.0.1:4444`
- Heartbeat toutes les 10 secondes (`HEARTBEAT`)
- Exécution de commandes shell via `subprocess.run(shell=True)`
- Reconnexion automatique si le contrôleur est absent

---

## Détection (Ware-Defender)

```bash
python3 -c "from modules.c2_detector import scan, print_report; print_report(scan())"
```

Alertes attendues :
- Connexion ESTABLISHED sur port `4444`
- Processus Python avec socket persistant vers IP externe

---

> ⚠️ Usage strictement réservé à un environnement de lab isolé.

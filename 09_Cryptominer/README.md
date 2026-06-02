# 09 — Cryptominer

> **Module Red Team** · Simulation d'un cryptominer furtif XMR

---

## Description

Simule un cryptominer Monero camouflé :
- Renomme le processus en `kworker/u:0` (imite un thread noyau)
- Lance 2 threads de hachage SHA-256 intensif (500 000 itérations)
- Tente des connexions TCP vers des pools miniers réels

---

## Fichiers

| Fichier | Rôle |
|---|---|
| `cryptominer_poc.py` | Mineur simulé (CPU + pool connections) |

---

## Usage

```bash
python3 cryptominer_poc.py        # 2 threads, 30 secondes
```

---

## Comportements simulés

| Comportement | Détail |
|---|---|
| Camouflage processus | `prctl(PR_SET_NAME, "kworker/u:0")` |
| CPU intensif | SHA-256 sur données aléatoires, 2 threads |
| Connexions pool | `pool.supportxmr.com:3333`, `xmrpool.eu:14444`... |

Les connexions réseau **échouent silencieusement** (pas de vrai minage).

---

## Détection (Ware-Defender)

```bash
python3 -c "from modules.cryptominer_detector import scan, print_report; print_report(scan())"
```

Alertes attendues :
- `miner_process` : `kworker` détecté par nom de processus
- `high_cpu_process` : CPU > 80% soutenu
- `mining_pool_connection` : tentative port 3333/4444

---

> ⚠️ Usage strictement réservé à un environnement de lab isolé.

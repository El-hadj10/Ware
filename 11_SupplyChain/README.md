# 11 — Supply Chain Attack

> **Module Red Team** · Simulation d'une attaque par typosquatting Python

---

## Description

Simule une attaque supply chain Python par typosquatting :
- Crée un faux paquet `requets` (imite `requests`) avec code malveillant
- Simule son import dans un environnement Python
- Laisse un marqueur d'infection dans `/tmp/.ware_supply_chain_poc`

---

## Fichiers

| Fichier | Rôle |
|---|---|
| `supply_chain_poc.py` | Création + import du faux paquet typosquat |

---

## Usage

```bash
python3 supply_chain_poc.py
```

---

## Comportement simulé

| Étape | Détail |
|---|---|
| **Création** | `requets/__init__.py` dans un répertoire temporaire |
| **Code injecté** | Crée `/tmp/.ware_supply_chain_poc`, affiche SHA256 |
| **Import** | `sys.path.insert` + `import requets` |
| **Nettoyage** | `TemporaryDirectory` → auto-supprimé à la fin |

Le vrai paquet `requests` **n'est pas modifié**.

---

## Détection (Ware-Defender)

```bash
python3 -c "from modules.supply_chain_detector import scan, print_report; print_report(scan())"
```

Alertes attendues :
- `infection_marker_found` : `/tmp/.ware_supply_chain_poc` détecté
- `typosquatted_package` : si `requets` est installé via pip
- `suspicious_package_code` : patterns `open("/tmp/"` dans `__init__.py`

---

> ⚠️ Usage strictement réservé à un environnement de lab isolé.

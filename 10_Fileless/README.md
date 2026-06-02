# 10 — Fileless Malware

> **Module Red Team** · Exécution de payload en mémoire pure (fileless)

---

## Description

Démontre les techniques d'exécution fileless sur Linux :
- Compilation et exécution de code Python directement en mémoire (`exec(compile())`)
- Création d'un fichier anonyme en RAM via `memfd_create` (syscall 319)
- Aucun artefact écrit sur le disque

---

## Fichiers

| Fichier | Rôle |
|---|---|
| `fileless_poc.py` | Démo d'exécution fileless + affichage des mappings mémoire |

---

## Usage

```bash
python3 fileless_poc.py
```

---

## Techniques simulées

| Technique | Détail |
|---|---|
| `exec(compile())` | Exécution d'un payload compilé en mémoire |
| `memfd_create` | Création d'un fd anonyme (`syscall 319` x86_64) via `ctypes` |
| `/proc/<pid>/maps` | Affichage des régions mémoire RWX créées |

Le payload est **inoffensif** (instructions `print` uniquement).

---

## Détection (Ware-Defender)

```bash
python3 -c "from modules.fileless_detector import scan, print_report; print_report(scan())"
```

Alertes attendues :
- `rwx_anonymous_region` : région mémoire RWX dans `/proc/maps`
- `memfd_descriptor` : fd `memfd:` ouvert
- `fileless_pattern_in_script` : `exec(compile(` dans `/tmp/`

---

> ⚠️ Usage strictement réservé à un environnement de lab isolé.

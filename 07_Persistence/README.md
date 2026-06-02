# 07 — Persistence

> **Module Red Team** · Installation de mécanismes de persistance Linux

---

## Description

Installe trois vecteurs de persistance classiques sur Linux afin de
garantir la survie du payload au redémarrage et à la déconnexion.

---

## Fichiers

| Fichier | Rôle |
|---|---|
| `persistence_poc.py` | Install / clean des 3 mécanismes |

---

## Usage

```bash
# Installer les 3 mécanismes de persistance
python3 persistence_poc.py

# Nettoyer tous les artefacts
python3 persistence_poc.py clean
```

---

## Mécanismes simulés

| Vecteur | Emplacement | Marqueur |
|---|---|---|
| Shell config | `~/.bashrc` | `# [WARE-PERSISTENCE]` |
| Crontab | `crontab -l` | `# ware-persistence-poc` |
| Autostart | `~/.config/autostart/ware-persistence.desktop` | `Exec=` pointant sur `/tmp/` |

Payload inoffensif : `echo '[WARE] Persistance active' > /tmp/.ware_alive`

---

## Détection (Ware-Defender)

```bash
python3 -c "from modules.persistence_detector import scan, print_report; print_report(scan())"
```

Alertes attendues :
- `shell_config_injection` dans `~/.bashrc`
- `suspicious_crontab_entry` avec `/tmp/`
- `suspicious_autostart` dans `~/.config/autostart/`

---

> ⚠️ Usage strictement réservé à un environnement de lab isolé.

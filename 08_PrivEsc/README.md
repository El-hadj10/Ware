# 08 — Privilege Escalation

> **Module Red Team** · Scan des vecteurs d'élévation de privilèges Linux

---

## Description

Identifie automatiquement les vecteurs PrivEsc exploitables sur le
système courant : binaires SUID dangereux, règles sudo permissives,
fichiers `/etc/` world-writable, et répertoires PATH détournables.

---

## Fichiers

| Fichier | Rôle |
|---|---|
| `privesc_poc.py` | Scanner de vecteurs PrivEsc |

---

## Usage

```bash
python3 privesc_poc.py
```

---

## Vecteurs analysés

| Vecteur | Méthode |
|---|---|
| **SUID GTFOBins** | `find /usr /bin /sbin -perm -4000` vs liste GTFOBins |
| **Sudo dangereux** | `sudo -l -n` → `NOPASSWD: ALL`, `NOPASSWD: /bin/bash`... |
| **PATH hijacking** | Répertoires du PATH world-writable |
| **World-writable /etc/** | `/etc/passwd`, `/etc/shadow`, `/etc/sudoers`... |

GTFOBins couverts : `bash`, `python`, `perl`, `find`, `vim`, `nmap`,
`tar`, `rsync`, `node`, `gdb`, `strace` et 12 autres.

---

## Détection (Ware-Defender)

```bash
python3 -c "from modules.privesc_detector import scan, print_report; print_report(scan())"
```

Alertes attendues :
- `suid_gtfobins` : liste des binaires exploitables trouvés
- `dangerous_sudo` si `NOPASSWD` présent
- `path_hijacking_risk` si `/tmp` dans PATH

---

> ⚠️ Usage strictement réservé à un environnement de lab isolé.

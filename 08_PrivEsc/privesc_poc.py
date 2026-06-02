#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 08: Privilege Escalation (PoC Éducatif)
Intention: Al-Alim (Connaître les failles d'élévation pour les refermer)
Description: Scanne les vecteurs classiques d'élévation de privilèges Linux :
             - Binaires SUID exploitables (GTFOBins)
             - Permissions sudo mal configurées
             - Variables PATH dangereuses (PATH hijacking)
             - Fichiers world-writable dans /etc/
Conformité: Flake8 / 88 caractères maximum.
"""

import os
import subprocess
import sys
from pathlib import Path

# Binaires SUID connus exploitables selon GTFOBins
GTFOBINS_SUID = {
    "bash", "sh", "python", "python3", "perl", "ruby", "php",
    "awk", "find", "nmap", "vim", "vi", "less", "more",
    "cp", "mv", "tee", "dd", "tar", "zip", "rsync",
    "node", "lua", "ftp", "gdb", "strace",
}


def scan_suid_binaries():
    """Cherche les binaires SUID potentiellement exploitables."""
    print("\n[PrivEsc] Scan des binaires SUID...")
    findings = []
    try:
        result = subprocess.run(
            ["find", "/usr", "/bin", "/sbin", "-perm", "-4000", "-type", "f"],
            capture_output=True, text=True, timeout=15
        )
        for line in result.stdout.splitlines():
            binary = Path(line).name
            if binary in GTFOBINS_SUID:
                findings.append(line)
                print(f"  [!] SUID exploitable (GTFOBins) : {line}")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("  [?] find indisponible.")
    if not findings:
        print("  [✓] Aucun SUID exploitable trouvé.")
    return findings


def scan_sudo_permissions():
    """Vérifie les permissions sudo de l'utilisateur courant."""
    print("\n[PrivEsc] Analyse des droits sudo...")
    try:
        result = subprocess.run(
            ["sudo", "-l", "-n"],
            capture_output=True, text=True, timeout=5
        )
        output = result.stdout + result.stderr
        dangerous = [
            line for line in output.splitlines()
            if any(b in line for b in GTFOBINS_SUID)
        ]
        if dangerous:
            for line in dangerous:
                print(f"  [!] Sudo dangereux : {line.strip()}")
        else:
            print("  [✓] Aucune entrée sudo dangereuse détectée.")
        return dangerous
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("  [?] sudo indisponible ou mot de passe requis.")
        return []


def scan_path_hijacking():
    """Détecte les répertoires world-writable dans le PATH."""
    print("\n[PrivEsc] Analyse du PATH pour hijacking...")
    path_dirs = os.environ.get("PATH", "").split(":")
    vulnerable = []
    for d in path_dirs:
        p = Path(d)
        if p.exists() and os.access(d, os.W_OK) and not p.is_symlink():
            # Monde entier en écriture ?
            mode = oct(p.stat().st_mode)[-3:]
            if mode[2] in ("7", "6", "3", "2"):
                vulnerable.append(d)
                print(f"  [!] Répertoire PATH world-writable : {d} ({mode})")
    if not vulnerable:
        print("  [✓] Aucun répertoire PATH world-writable.")
    return vulnerable


def scan_world_writable_etc():
    """Cherche les fichiers world-writable critiques dans /etc/."""
    print("\n[PrivEsc] Scan des fichiers world-writable dans /etc/...")
    sensitive = [
        "/etc/passwd", "/etc/shadow", "/etc/sudoers",
        "/etc/crontab", "/etc/environment",
    ]
    findings = []
    for f in sensitive:
        p = Path(f)
        if p.exists():
            mode = oct(p.stat().st_mode)[-3:]
            if mode[2] in ("7", "6", "3", "2"):
                findings.append(f)
                print(f"  [!] Fichier critique world-writable : {f} ({mode})")
    if not findings:
        print("  [✓] Aucun fichier /etc/ critique en world-writable.")
    return findings


if __name__ == "__main__":
    print("=" * 55)
    print(" WARE — PrivEsc Scanner (PoC Éducatif)")
    print("=" * 55)
    suid = scan_suid_binaries()
    sudo_issues = scan_sudo_permissions()
    path_issues = scan_path_hijacking()
    etc_issues = scan_world_writable_etc()

    total = len(suid) + len(sudo_issues) + len(path_issues) + len(etc_issues)
    print(f"\n[Résumé] {total} vecteur(s) d'élévation potentiel(s) détecté(s).")
    sys.exit(0 if total == 0 else 1)

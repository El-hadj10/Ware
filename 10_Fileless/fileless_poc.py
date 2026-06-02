#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 10: Fileless Malware (PoC Éducatif)
Intention: Al-Fattah (Comprendre les attaques sans fichier pour les détecter)
Description: Simule un malware fileless sous Linux :
             - Charge le payload uniquement en mémoire via memfd_create
             - N'écrit aucun fichier exécutable sur le disque
             - Le payload est visible dans /proc/<pid>/maps comme
               région RWX anonyme
Conformité: Flake8 / 88 caractères maximum.
"""

import ctypes
import ctypes.util
import os

# Payload inoffensif (simulation d'audit mémoire)
PAYLOAD_SOURCE = """
import os
print(f"[Fileless-Payload] PID={os.getpid()} — exécution en mémoire pure.")
print("[Fileless-Payload] Aucun fichier écrit sur le disque.")
"""


def memfd_create_payload(name=b"ware_poc"):
    """
    Crée un fichier anonyme en mémoire via memfd_create(2).
    Retourne le file descriptor ou None si non disponible.
    Uniquement disponible sur Linux kernel >= 3.17.
    """
    libc_name = ctypes.util.find_library("c")
    if not libc_name:
        return None
    libc = ctypes.CDLL(libc_name, use_errno=True)
    # syscall memfd_create = 319 sur x86_64
    try:
        fd = libc.syscall(319, name, 1)  # MFD_CLOEXEC = 1
        if fd < 0:
            return None
        return fd
    except Exception:
        return None


def execute_in_memory():
    """
    Exécute le payload Python directement en mémoire.
    Simule l'absence totale d'artefacts disque.
    """
    print("[Fileless] Tentative d'exécution en mémoire pure...")

    # Méthode 1 : exec() direct (Python in-process, pas de fichier)
    print("[Fileless] Méthode exec() Python in-process :")
    local_ns = {}
    exec(compile(PAYLOAD_SOURCE, "<memoire>", "exec"), local_ns)

    # Méthode 2 : simulation memfd_create (montre le fd anonyme)
    fd = memfd_create_payload()
    if fd is not None:
        payload_bytes = PAYLOAD_SOURCE.encode("utf-8")
        os.write(fd, payload_bytes)
        print(
            f"[Fileless] memfd_create réussi : fd={fd}"
            f" visible dans /proc/{os.getpid()}/fd/{fd}"
        )
        print(
            "[Fileless] Un outil forensique trouverait une région "
            "anonyme RWX dans /proc/maps."
        )
        os.close(fd)
    else:
        print(
            "[Fileless] memfd_create indisponible sur ce noyau "
            "(nécessite Linux >= 3.17 x86_64)."
        )


def show_proc_maps():
    """Affiche les régions mémoire anonymes du processus courant."""
    maps_file = f"/proc/{os.getpid()}/maps"
    try:
        with open(maps_file, encoding="utf-8") as f:
            lines = f.readlines()
        anon_rwx = [
            line for line in lines
            if "rwx" in line and (line.strip().endswith("[anon]") or line.split()[-1] == "")
        ]
        if anon_rwx:
            print("\n[Fileless] Régions RWX anonymes dans /proc/maps :")
            for line in anon_rwx[:5]:
                print(f"  {line.rstrip()}")
        else:
            print("\n[Fileless] Aucune région RWX anonyme trouvée (normal).")
    except OSError:
        pass


if __name__ == "__main__":
    execute_in_memory()
    show_proc_maps()
    print("\n[Fileless] PoC terminé — aucun fichier créé sur le disque.")

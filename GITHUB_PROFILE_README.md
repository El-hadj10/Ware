<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0000,30:1a0000,70:2d0505,100:0f0a00&height=220&section=header&text=W%20A%20R%20E&fontSize=78&fontColor=cc2222&animation=fadeIn&fontAlignY=36&desc=Traité%20d'Architecture%20Offensive%20—%2011%20Modules%20·%20Red%20Team%20Lab&descAlignY=60&descSize=16&descColor=884444" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/psutil-5.9.8-cc2222?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Flake8-Conforme-00cc66?style=for-the-badge" />
  <img src="https://img.shields.io/badge/GoDo-Framework-882200?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Usage-Lab_Isolé_Uniquement-cc2200?style=for-the-badge&logo=shield&logoColor=white" />
</p>

<p align="center">
  <a href="https://github.com/El-hadj10/Ware">
    <img src="https://img.shields.io/badge/Dépôt-El--hadj10%2FWare-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/El-hadj10/Ware-Defender">
    <img src="https://img.shields.io/badge/Blue_Team-Ware--Defender-0044cc?style=for-the-badge&logo=shield&logoColor=white" />
  </a>
  <img src="https://img.shields.io/badge/Modules-11-cc2222?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Statut-Complet-00cc44?style=for-the-badge" />
</p>

---

## ⚔️ Présentation

**Ware** est un traité d'architecture offensive en Python qui simule les 11 grandes familles de logiciels malveillants modernes. Chaque module est un PoC autonome, confiné, documenté et validé par flake8. Le projet est le pendant offensif de **[Ware-Defender](https://github.com/El-hadj10/Ware-Defender)**.

```
╔══════════════════════════════════════════════════════════════════╗
║  ⚔️  WARE  — Red Team Architecture Lab                          ║
║  Auteur    : Nour  (El-hadj10)                                   ║
║  Langage   : Python 3.12  ·  Linux uniquement                    ║
║  Framework : GoDo (.qodo)  ·  flake8 max-line 88 chars           ║
║  Doctrine  : Al-Basir — Voir l'attaque pour mieux la bloquer     ║
║  Modules   : 11 PoC  ·  11 Agents GoDo  ·  3 Workflows          ║
╚══════════════════════════════════════════════════════════════════╝
```

> *"On ne défend pas ce que l'on ne comprend pas. Chaque PoC est une lumière portée sur l'ombre."*

---

## 📁 Architecture du Projet

```
Ware/
├── 01_Keylogger/            ─ Capture frappes clavier · pynput · buffer disque
├── 02_Spyware/              ─ Exfiltration profil user · .ssh · .env · notes
├── 03_Worm/                 ─ Propagation réseau · scan LAN · pseudo-copie SSH
├── 04_Ransomware/           ─ Chiffrement AES-256 · Fernet · clé exportable
├── 05_Malware_IA/           ─ Moteur polymorphique · mutation de signature · IA locale
├── 06_Backdoor_C2/          ─ Canal TCP C2 · heartbeat · reverse shell confiné
├── 07_Persistence/          ─ 3 mécanismes : bashrc · crontab · autostart .desktop
├── 08_PrivEsc/              ─ GTFOBins SUID · sudo NOPASSWD · world-writable /etc/
├── 09_Cryptominer/          ─ kworker camouflé · SHA-256 intensif · pools XMR simulés
├── 10_Fileless/             ─ exec(compile()) · memfd_create · /proc/maps RWX
├── 11_SupplyChain/          ─ Typosquat 'requets' · hook __init__.py · import dynamique
├── .qodo/
│   ├── agents/              ─ 11 fichiers godo_agent.json  (type: "attack")
│   └── workflows/           ─ qodo_resonance.py · godo_orchestrator.py · validate_agents.py
├── requirements.txt         ─ pynput · cryptography · psutil · colorama
├── setup.sh                 ─ Installation automatique · venv Python
└── README.md                ─ Documentation principale
```

---

## 🗺️ Les 11 Modules

| # | Module | Technique simulée | Fichier PoC | Détecteur associé |
|---|--------|-------------------|-------------|-------------------|
| 01 | **Keylogger** | Capture frappes · pynput listener · buffer disque | `keylogger_poc.py` | `keylogger_detector.py` |
| 02 | **Spyware** | Walk profil user · .ssh · .env · notes · SHA-256 | `infostealer_poc.py` | `spyware_detector.py` |
| 03 | **Worm** | Scan subnet LAN · socket · propagation simulée SSH | `worm_poc.py` | `worm_detector.py` |
| 04 | **Ransomware** | AES-256 Fernet · chiffrement récursif · clé exportée | `ransomware_encrypt.py` | `ransomware_detector.py` |
| 05 | **Malware_IA** | Moteur polymorphique · mutation SHA-256 · padding crypto | `polymorphic_engine.py` | `ia_detector.py` |
| 06 | **Backdoor_C2** | TCP 4444 · heartbeat · reconnexion · subprocess shell | `backdoor_c2_poc.py` | `c2_detector.py` |
| 07 | **Persistence** | bashrc injection · crontab · autostart .desktop | `persistence_poc.py` | `persistence_detector.py` |
| 08 | **PrivEsc** | 23 GTFOBins SUID · sudo NOPASSWD · world-writable /etc/ | `privesc_poc.py` | `privesc_detector.py` |
| 09 | **Cryptominer** | prctl kworker · SHA-256 x500k · pools XMR (socket) | `cryptominer_poc.py` | `cryptominer_detector.py` |
| 10 | **Fileless** | exec(compile()) · memfd_create · /proc/maps RWX | `fileless_poc.py` | `fileless_detector.py` |
| 11 | **SupplyChain** | Typosquat 'requets' · hook __init__ · sys.path.insert | `supply_chain_poc.py` | `supply_chain_detector.py` |

---

## 🌐 Vue Hub-and-Spoke — Architecture Offensive

<table>
<tr>
<td align="center" width="220">

**01 — KEYLOGGER**

Listener `pynput.keyboard`
Buffer mémoire (100 events)
Flush → `keylog_buffer.txt`
Timeout 30s · auto-stop
Frappes spéciales capturées

</td>
<td align="center" width="220">

**02 — SPYWARE**

Walk récursif profil user
Cibles : `.ssh/`, `.env`, notes
SHA-256 par fichier affiché
Profil fictif inclus pour démo
Aucune exfiltration réseau

</td>
<td align="center" width="220">

**03 — WORM**

Scan subnet /24 via socket
Détection hôtes actifs
Simulation SSH sans auth
Liste targets `/tmp/.ware_targets`
Nettoyage automatique

</td>
</tr>
<tr>
<td align="center">

**04 — RANSOMWARE**

AES-256 via `cryptography.fernet`
Chiffrement récursif `vault_documents/`
Clé exportée séparément
`ransomware_decrypt.py` inclus
Vault fictif de démonstration

</td>
<td align="center">

**05 — MALWARE_IA**

`polymorphic_engine.py`
Moteur polymorphique IA
Mutation signature SHA-256
Dérive contrôlée du hash
Padding aléatoire crypto

</td>
<td align="center">

**06 — BACKDOOR_C2**

Agent TCP sur 127.0.0.1:4444
Contrôleur séparé (localhost)
Heartbeat `[HEARTBEAT] Agent actif`
Reconnexion auto (3 essais)
Commandes via `subprocess`

</td>
</tr>
<tr>
<td align="center">

**07 — PERSISTENCE**

Injection `~/.bashrc` + marqueur
Crontab `*/5 * * * *` `/tmp/.ware_alive`
`.desktop` dans `~/.config/autostart/`
Fonction `clean_all()` rollback
Aucune persistance sans appel

</td>
<td align="center">

**08 — PRIVESC**

23 GTFOBins dans la liste SUID
`sudo -l -n` → analyse NOPASSWD
8 chemins world-writable /etc/
PATH hijacking (dirs writables)
Scan passif — aucune élévation

</td>
<td align="center">

**09 — CRYPTOMINER**

`prctl(15, b"kworker/u:0")` camouflage
2 threads SHA-256 · 500k iterations
Sockets vers pools XMR (refusés)
`threading.Event` stop à 30s
CPU spike détectable par psutil

</td>
</tr>
<tr>
<td align="center">

**10 — FILELESS**

`exec(compile(PAYLOAD_SOURCE, ...))`
`memfd_create(b"ware_memfd", 1)` ctypes
Affichage régions /proc/maps RWX
Fd anonyme fermé proprement
Aucun artefact disque

</td>
<td align="center">

**11 — SUPPLY CHAIN**

Paquet typosquat `requets`
Hook `/tmp/.ware_supply_chain_poc`
`sys.path.insert` + import dynamique
`TemporaryDirectory` → nettoyage auto
SHA-256 du paquet affiché

</td>
</tr>
</table>

---

## 🤖 GoDo Framework — 11 Agents Attack

Le framework `.qodo` orchestre les agents IA offensifs. Chaque module dispose d'un `godo_agent.json` de type `"attack"` avec 5 tâches documentées.

```
.qodo/
├── agents/
│   ├── Keylogger/godo_agent.json        ─ type: "attack" · 5 tasks
│   ├── Spyware/godo_agent.json          ─ type: "attack" · 5 tasks
│   ├── Worm/godo_agent.json             ─ type: "attack" · 5 tasks
│   ├── Ransomware/godo_agent.json       ─ type: "attack" · 5 tasks
│   ├── Malware_IA/godo_agent.json       ─ type: "attack" · 5 tasks
│   ├── Backdoor_C2/godo_agent.json      ─ type: "attack" · 5 tasks
│   ├── Persistence/godo_agent.json      ─ type: "attack" · 5 tasks
│   ├── PrivEsc/godo_agent.json          ─ type: "attack" · 5 tasks
│   ├── Cryptominer/godo_agent.json      ─ type: "attack" · 5 tasks
│   ├── Fileless/godo_agent.json         ─ type: "attack" · 5 tasks
│   └── SupplyChain/godo_agent.json      ─ type: "attack" · 5 tasks
└── workflows/
    ├── qodo_resonance.py                ─ Dashboard chromatique · jauge par agent
    ├── godo_orchestrator.py             ─ Simulation cycle de vie des tâches
    └── validate_agents.py               ─ Validation structure JSON des 11 agents
```

**Structure JSON d'un Agent :**

```json
{
  "name": "Backdoor_C2",
  "description": "Simule un agent C2 reverse shell TCP sur 127.0.0.1:4444 avec heartbeat.",
  "type": "attack",
  "module": "06_Backdoor_C2",
  "tasks": [
    {"title": "Implémenter le canal TCP C2 agent/contrôleur", "status": "Terminé"},
    {"title": "Ajouter le heartbeat et la reconnexion automatique", "status": "Terminé"},
    {"title": "Exécuter les commandes shell via subprocess", "status": "Terminé"},
    {"title": "Tester la détection par c2_detector.py", "status": "À faire"},
    {"title": "Documenter le scénario dans training/README.md", "status": "Terminé"}
  ]
}
```

```bash
# Dashboard GoDo chromatique (11 jauges de progression)
python3 .qodo/workflows/qodo_resonance.py

# Valider la structure des 11 agents
python3 .qodo/workflows/validate_agents.py

# Orchestrer un cycle de simulation
python3 .qodo/workflows/godo_orchestrator.py
```

---

## 🛠️ Stack Technique

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/pynput-1.7.7-cc4400?style=for-the-badge" />
  <img src="https://img.shields.io/badge/cryptography-42.0-882200?style=for-the-badge" />
  <img src="https://img.shields.io/badge/psutil-5.9.8-aa3300?style=for-the-badge" />
  <img src="https://img.shields.io/badge/colorama-0.4.6-ffaa00?style=for-the-badge" />
  <img src="https://img.shields.io/badge/flake8-7.0-00cc66?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/ctypes-Linux_Syscalls-cc2222?style=for-the-badge" />
  <img src="https://img.shields.io/badge/subprocess-Shell_Exec-882200?style=for-the-badge" />
  <img src="https://img.shields.io/badge/threading-Multi--Thread-aa3300?style=for-the-badge" />
  <img src="https://img.shields.io/badge/socket-TCP_Réseau-cc4400?style=for-the-badge" />
</p>

---

## ⚙️ Installation & Usage

```bash
git clone https://github.com/El-hadj10/Ware.git
cd Ware

# Installation automatique (venv + pip)
bash setup.sh

# Ou manuellement
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

```bash
source venv/bin/activate

# Exécuter un module individuellement
python3 01_Keylogger/keylogger_poc.py
python3 06_Backdoor_C2/backdoor_c2_poc.py
python3 09_Cryptominer/cryptominer_poc.py

# Dashboard GoDo
python3 .qodo/workflows/qodo_resonance.py
```

---

## ⚖️ Doctrine Éthique

> ⚠️ **Usage strictement réservé à un environnement de laboratoire isolé.**

Chaque module de Ware :
- Ne touche que le système local (`127.0.0.1`, `/tmp`, home utilisateur)
- Inclut une fonction de nettoyage ou un rollback automatique
- Est documenté avec ses patterns de détection précis
- N'établit aucune connexion vers un serveur externe réel

**Son pendant défensif :** [Ware-Defender](https://github.com/El-hadj10/Ware-Defender)

---

## 🔗 Liens

<p align="center">
  <a href="https://github.com/El-hadj10/Ware">
    <img src="https://img.shields.io/badge/Dépôt_GitHub-Ware-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/El-hadj10/Ware-Defender">
    <img src="https://img.shields.io/badge/Blue_Team-Ware--Defender-0044cc?style=for-the-badge&logo=shield&logoColor=white" />
  </a>
  <a href="https://github.com/El-hadj10">
    <img src="https://img.shields.io/badge/Auteur-El--hadj10-cc2222?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0000,50:1a0000,100:0a0000&height=120&section=footer" width="100%" />
</p>

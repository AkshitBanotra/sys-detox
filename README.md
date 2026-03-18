<div align="center">
 
# ☠ sys-detox
 
> *The grid doesn't care about your willpower. So you automate it.*
 
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
 
A CLI focus daemon for Linux. Kills distracting apps, locks you in, and lets you breathe on a timer — wired into systemd so it runs in the background like it should.
 
**No GUI. No hand-holding. Just signal and noise.**
 
</div>
 
---
 
## Features
 
- 🔒 **Focus mode** — kills distracting processes (Steam, Lutris, and whatever else you configure)
- ⏱ **Timed breaks** — request a break window, it pulls you back when time's up
- 📋 **Status at a glance** — see your current mode and remaining time instantly
- 🔧 **systemd integration** — runs as a user service, persists across sessions
- 🔔 **Notifications + audio cues** — via `notify-send` and `paplay`
- ⚙️ **Simple config** — single JSON file, easy to modify
 
---
 
## Requirements
 
**Python**
| Package | Purpose |
|---------|---------|
| `rich` | Terminal output formatting |
 
**System**
| Tool | Purpose |
|------|---------|
| `systemd` | Background daemon management |
| `notify-send` | Desktop notifications |
| `paplay` | Audio cues |
| `pkill` | Process termination |
 
---
 
## Installation
 
> **Note:** An automated install script is planned. For now, set it up manually — it takes under a minute.
 
```bash
# 1. Clone the repo into your home directory
git clone https://github.com/AkshitBanotra/sys-detox.git ~/sys-detox
cd ~/sys-detox
 
# 2. Install the Python dependency
pip install rich
 
# 3. Make the script executable and strip the .py extension
chmod +x sys-detox.py
mv sys-detox.py sys-detox
 
# 4. Move it to ~/.local/bin
mkdir -p ~/.local/bin
cp sys-detox ~/.local/bin/sys-detox
 
# 5. Add ~/.local/bin to PATH (if not already)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
 
# 6. Run first-time setup
sys-detox setup
```
 
After this, `sys-detox` works as a regular command from anywhere in your terminal.
 
---
 
## Usage
 
### `setup` — First-time initialization
```bash
sys-detox setup
```
Registers the systemd user service. **Run once.**
 
---
 
### `status` — Check current mode
```bash
sys-detox status
```
Displays whether you're in **focus** or **break** mode, and remaining session time if active.
 
---
 
### `break` — Take a timed break
```bash
sys-detox break <minutes>
```
Suspends focus mode for the given number of minutes. Blocked apps are unkilled during the window. When the timer expires, focus mode kicks back in automatically.
 
```bash
sys-detox break 60   # Example: 60 minutes breather
```
 
---
 
## Config
 
Located at `~/sys-detox/config.json`.
 
```json
{
  "mode": "focus",
  "time": 25
}
```
 
| Key | Values | Description |
|-----|--------|-------------|
| `mode` | `"focus"` / `"break"` | Current active mode |
| `time` | integer (minutes) | Session duration |
 
To block additional apps, find the `pkill` targets in the source and append your own process names. If it has a process name, it can be killed.
 
---
 
## How It Works
 
```
sys-detox (CLI)
    │
    ├── argparse ──────────→ routes subcommands
    │
    ├── setup ─────────────→ writes systemd unit files
    │                    
    │
    ├── status ────────────→ reads config.json
    │                        queries systemd service state
    │                        renders via rich
    │
    └── break ─────────────→ updates config.json
                             signals systemd service
                             countdown via time module
                             notify-send + paplay for alerts
                             auto-reverts to focus on expiry
```
 
The daemon runs as a **systemd user service** — no root required. State is managed via a JSON file over IPC. `subprocess` bridges Python to the shell, delegating OS operations like process termination and service management.

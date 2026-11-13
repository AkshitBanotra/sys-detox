# sys-detox

A Linux CLI utility for managing focus sessions and timed breaks by automatically terminating configured distracting processes.

## Features

- **Focus mode:** Terminates configured processes.
- **Timed breaks:** Temporarily suspends process monitoring.
- **Session status:** Displays the current mode and remaining time.
- **systemd integration:** Runs as a user-level background service.
- **Notifications:** Desktop notifications and audio alerts.
- **Configuration:** JSON-based configuration.

## Requirements

| Dependency | Purpose |
|---|---|
| Python 3.8+ | Runtime |
| `rich` | Terminal formatting |
| `systemd` | Background service |
| `notify-send` | Desktop notifications |
| `paplay` | Audio alerts |
| `pkill` | Process management |

## Installation

```bash
git clone https://github.com/AkshitBanotra/sys-detox.git
cd sys-detox

pip install rich

chmod +x sys-detox.py
mv sys-detox.py sys-detox

mkdir -p ~/.local/bin
cp sys-detox ~/.local/bin/

export PATH="$HOME/.local/bin:$PATH"

sys-detox setup
```

## Usage

| Command | Description |
|---|---|
| `sys-detox setup` | Initialize the systemd service |
| `sys-detox status` | Display the current session status |
| `sys-detox break <minutes>` | Start a timed break |

Example:

```bash
sys-detox break 60
```

## Configuration

Configuration is stored in `~/sys-detox/config.json`.

```json
{
  "mode": "focus",
  "time": 25
}
```

| Key | Description |
|---|---|
| `mode` | Current mode: `focus` or `break` |
| `time` | Session duration in minutes |

Additional processes can be configured by modifying the process targets in the source code.

## Architecture

```text
CLI
 ├── Argument parsing
 ├── Configuration management
 ├── systemd service
 │    └── Background process monitoring
 ├── Process management
 └── Notifications and audio alerts
```

The utility uses a systemd user service to manage background execution without requiring root privileges. Configuration is maintained through a JSON file, while Python's `subprocess` module handles system-level operations.

## License

MIT

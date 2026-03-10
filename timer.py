#!/usr/bin/env python3

from subprocess import run
import time
from rich import print
from os import environ
import json

#####################################################

home = environ["HOME"]
json_path = f"{home}/sys-detox/config.json"
sound_path1 = f"{home}/sys-detox/sounds/Mallet.ogg"
sound_path2 = f"{home}/sys-detox/sounds/fantasy.mp3"

#####################################################

run(["systemctl", "--user", "stop", "sys-detox"])
run(["notify-send", "SYS-DETOX", "Game Mode started! 🎮"])
run(["paplay", sound_path1])
with open(json_path, "r") as f:
    data = json.load(f)
i = data["time"]
while i > 0:
    # print(f"\r[bold cyan]Game Until: {i:02d} minutes[/bold cyan]", end='',flush=True)
    data["time"] = i
    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)
    time.sleep(60)
    i -= 1
data["mode"] = "Focus"
with open(json_path, "w") as f:
    json.dump(data, f, indent=4)
run(["notify-send", "SYS-DETOX", "Exiting Game Mode..."])
run(["paplay", sound_path2])
run(["systemctl", "--user", "start", "sys-detox"])

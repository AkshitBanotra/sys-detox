#!/usr/bin/env python3

import argparse
import json
import subprocess
from rich import print

######################################

# Parsing argparse

parser = argparse.ArgumentParser(
        description="sys-detox - Block distractions and stay focussed! :D"
        )
subparsers = parser.add_subparsers(dest="option")

subparsers.add_parser("setup", help="setup sys-detox service")
subparsers.add_parser("status", help="check current mode")

game_parser = subparsers.add_parser("break", help="Switch to Break mode") # Created break argument which needs timer argument too!
game_parser.add_argument("timer", type=int, help="Duration in minutes")
args = parser.parse_args()

# Loading config.json for state switching

with open("config.json") as f:
    data = json.load(f)

if args.option == "setup":
    subprocess.run(["./setup.sh"])
elif args.option == "break":
    data["mode"] = "Break"
    data["time"] = args.timer
    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)
    subprocess.Popen(["python3", "timer.py", str(args.timer)])
elif args.option is None:
    parser.print_help()
elif args.option == "status":
    if data["mode"] == "Focus":
        print(f"[bold cyan]{'Mode -':<10}[/bold cyan] [bold green]{data["mode"]}[/bold green]")
    elif data["mode"] == "Break":
        print(f"[bold cyan]{'Mode -':<10}[/bold cyan] [bold red]{data["mode"]}[/bold red]")
        print(f"[bold blue]{'Time Until -':<10}[/bold blue] [bold yellow]{data["time"]}[/bold yellow]")
else:
    print(f"[bold red]Invalid Command! Use --help or -h for options.[/bold red]")

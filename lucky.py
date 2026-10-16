#!/usr/bin/env python3
"""
LUCKY — a themed terminal shell.

Boot animation -> password gate (1234) -> a tiny shell with a
neofetch-style report and a handful of custom commands.

Works anywhere Python 3 runs: Termux on Android, or a normal
terminal on Linux / macOS / Windows.

    python3 lucky.py
"""
import getpass
import os
import platform
import random
import shutil
import sys
import time

GREEN, BOLD, RESET = "\033[92m", "\033[1m", "\033[0m"
CLEAR = "\033[2J\033[H"
PASSWORD = "1234"
START_TIME = time.time()

BANNER_BIG = r"""
██╗     ██╗   ██╗ ██████╗██╗  ██╗██╗   ██╗
██║     ██║   ██║██╔════╝██║ ██╔╝╚██╗ ██╔╝
██║     ██║   ██║██║     █████╔╝  ╚████╔╝ 
██║     ██║   ██║██╔═██╗   ╚██╔╝  
███████╗╚██████╔╝╚██████╗██║  ██╗   ██║   
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝
"""

BANNER_SMALL = r"""
 _    _   _  ____ _  ____   __
| |  | | | |/ ___| |/ /\ \ / /
| |  | | | | |   | ' /  \ V /
| |__| |_| | |___| . \   | |
|____\___/\____|_|\_\  |_|
"""

# A spiral generated from an Archimedean-spiral equation (not traced from
# Debian's trademarked artwork) — a big version for the boot flash, and a
# compact one sized to sit beside the stats in `neofetch`.
SWIRL = r"""
                                 .@@@.
                                   .@@.
                                    .@@.
                                     .@@.
              ..                      .@@.
         ...@@@@@@...                 .@@.
      ..@@@@@....@@@@..               ..@@.
     ..@@@..      .@@@.                .@@.
    ..@@..         .@@.               ..@@.
    .@@..                             ..@..
   ..@@..                             .@@.
   ..@@..                            .@@..
    .@@..                           .@@@.
    ..@@..                        ..@@@.
     ..@@@.                     ..@@@..
       .@@@...                ..@@@..
        ..@@@@.....     .....@@@@..
           ...@@@@@@@@@@@@@@@...
               ............
                D E B I A N
"""

SWIRL_SMALL = r"""
                    @@@
                     @@@
       @@@            @@
   @@@@@@@@@@          @
  @@@@    @@@@         @
 @@@@     @@@          @
 @@@                  @@
 @@@                 @@@
  @@@@             @@@@
   @@@@@         @@@@@
     @@@@@@@@@@@@@@
          @@@@
"""

# A simple figure that glitches apart, frame by frame. Kept abstract on
# purpose instead of redrawing the character from your photo, since that
# art is somebody else's copyrighted work.
GLITCH_FRAMES = [
    "      o\n     /|\\\n     / \\",
    "      o\n     /#\\\n     %#\\",
    "      %\n     #%#\n     %#%",
    "      .\n     . .\n      .",
    "",
]


def enable_ansi():
    if platform.system() == "Windows":
        os.system("")  # turns on ANSI escape handling in modern cmd/PowerShell


def slow_print(text, delay=0.01):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def get_banner():
    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    return BANNER_BIG if width >= 60 else BANNER_SMALL


def boot_sequence():
    print(CLEAR + GREEN + BOLD + get_banner() + RESET)
    time.sleep(0.6)

    for line in [
        "[ OK ] Starting lucky-core...",
        "[ OK ] Mounting /dev/null to /dev/null",
        "[ OK ] Loading green phosphor driver",
        "[ OK ] Calibrating signal",
        "[WARN] Unknown presence detected on stdin",
    ]:
        slow_print(GREEN + line + RESET, 0.006)
        time.sleep(0.12)
    time.sleep(0.3)

    for frame in GLITCH_FRAMES:
        print(CLEAR + GREEN + frame + RESET)
        time.sleep(0.15)
    time.sleep(0.2)

    for _ in range(3):
        print(CLEAR + GREEN + BOLD + SWIRL + RESET)
        time.sleep(0.15)
        print(CLEAR)
        time.sleep(0.1)
    print(CLEAR + GREEN + BOLD + SWIRL + RESET)
    time.sleep(0.3)


def password_gate(tries=3):
    for attempt in range(tries):
        try:
            guess = getpass.getpass(GREEN + "Enter password: " + RESET)
        except Exception:
            guess = input(GREEN + "Enter password: " + RESET)
        if guess == PASSWORD:
            print(GREEN + "\nAccess granted.\n" + RESET)
            return True
        print(GREEN + f"Incorrect. {tries - attempt - 1} attempt(s) left." + RESET)
    print(GREEN + "ACCESS DENIED." + RESET)
    return False


def neofetch():
    user, host = getpass.getuser(), platform.node() or "lucky"
    info = [
        f"{BOLD}{user}{RESET}{GREEN}@{BOLD}{host}{RESET}",
        GREEN + "-" * (len(user) + len(host) + 1),
        f"OS: {platform.system()} {platform.release()}",
        f"Shell: {os.environ.get('SHELL') or os.environ.get('COMSPEC', 'unknown')}",
        f"CPU: {platform.processor() or 'unknown'} ({os.cpu_count()} cores)",
        f"Python: {platform.python_version()}",
        f"Uptime: {time.strftime('%H:%M:%S', time.gmtime(time.time() - START_TIME))} (session)",
    ]
    logo_lines = SWIRL_SMALL.strip("\n").split("\n")
    print()
    for i in range(max(len(logo_lines), len(info))):
        left = logo_lines[i] if i < len(logo_lines) else ""
        right = info[i] if i < len(info) else ""
        print(f"{GREEN}{left:<24}{RESET} {right}")
    print()


FILES = {
    "readme.md": "you made it in. type 'help' to look around.",
    "secrets.txt": "nice try. there's nothing here. :)",
    "notes.txt": "TODO: actually put secrets somewhere else.",
}


def cmd_matrix():
    cols = shutil.get_terminal_size(fallback=(80, 24)).columns
    try:
        for _ in range(60):
            line = "".join(random.choice("01") if random.random() < 0.3 else " " for _ in range(cols))
            print(GREEN + line + RESET)
            time.sleep(0.03)
    except KeyboardInterrupt:
        pass


HELP = (GREEN + "commands: help, neofetch, whoami, date, echo, ls, cat, "
        "banner, matrix, clear, lock, exit" + RESET)


def main():
    enable_ansi()
    boot_sequence()
    if not password_gate():
        sys.exit(1)

    while True:
        try:
            raw = input(GREEN + "lucky" + RESET + ":~$ ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not raw:
            continue
        cmd, *args = raw.split()
        cmd = cmd.lower()

        if cmd in ("exit", "quit"):
            print(GREEN + "logging out." + RESET)
            break
        elif cmd == "help":
            print(HELP)
        elif cmd == "neofetch":
            neofetch()
        elif cmd == "whoami":
            print(getpass.getuser())
        elif cmd in ("clear", "cls"):
            print(CLEAR, end="")
        elif cmd == "date":
            print(time.strftime("%a %b %d %H:%M:%S %Y"))
        elif cmd == "echo":
            print(" ".join(args))
        elif cmd == "ls":
            print("  ".join(FILES))
        elif cmd == "cat":
            if not args:
                print("usage: cat <file>")
            else:
                print(FILES.get(args[0], f"cat: {args[0]}: no such file"))
        elif cmd == "banner":
            print(GREEN + get_banner() + RESET)
        elif cmd == "matrix":
            cmd_matrix()
        elif cmd == "lock":
            if not password_gate():
                sys.exit(1)
        else:
            print(f"lucky: command not found: {cmd}")


if __name__ == "__main__":
    main()

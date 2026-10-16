# Lucky

A themed terminal shell: a boot animation, a password gate, a neofetch-style
system report, and a handful of custom commands — all in green-on-black,
all in one Python file. Runs the same on Termux (Android) and on a normal
terminal on Linux, macOS, or Windows.

## What happens when you run it

1. The LUCKY banner prints (compact on narrow terminals, full-size on wide ones).
2. A short boot log scrolls by.
3. A small ASCII figure glitches apart.
4. A spiral logo flashes a few times.
5. You're asked for a password.
6. Correct password → dropped into a tiny shell with its own commands.

## Requirements

- Python 3.7 or newer (no extra packages needed — standard library only)

## Install & run

### Android (Termux)

```bash
pkg update && pkg install python git -y
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python lucky.py
```

### Linux / macOS

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python3 lucky.py
```

### Windows (cmd, PowerShell, or Windows Terminal)

Install Python from [python.org](https://www.python.org/downloads/) first,
and check **"Add python.exe to PATH"** during setup. Then:

```powershell
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python lucky.py
```

No `git`? Just download `lucky.py` directly from the repo page and run it
the same way — the script is self-contained.

## Password

Default password is **`1234`**. To change it, open `lucky.py` and edit:

```python
PASSWORD = "1234"
```

> This is a cosmetic gate for a fun terminal toy, not real security — the
> password lives in plain text in the script, so don't use it to protect
> anything that actually matters.

## Commands

Once you're in:

| Command | What it does |
|---|---|
| `help` | List available commands |
| `neofetch` | Show a system report next to the logo |
| `whoami` | Print the current username |
| `date` | Print the current date and time |
| `echo <text>` | Print text back |
| `ls` | List the fake files in the shell |
| `cat <file>` | Print the contents of a fake file |
| `banner` | Reprint the LUCKY banner |
| `matrix` | A short falling-code animation |
| `clear` / `cls` | Clear the screen |
| `lock` | Re-lock and ask for the password again |
| `exit` / `quit` | Leave the shell |

## License

Add a license of your choice (MIT is a common, permissive pick for a small
script like this) — GitHub can generate one for you when creating the repo,
or add a `LICENSE` file afterward.

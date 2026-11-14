#!/usr/bin/env python3

from pathlib import Path
import subprocess


def netzwerkanschluesse_suchen():
    print("========================================")
    print(" Linux Druckerassistent 1.0")
    print(" Physische Netzwerkanschluesse")
    print("========================================")
    print()

    netzwerkordner = Path("/sys/class/net")
    gefunden = 0

    for anschluss in sorted(netzwerkordner.iterdir()):
        # Virtuelle Netzwerkanschluesse ausschliessen
        if not (anschluss / "device").exists():
            continue

        # Nur Ethernet-Anschluesse beruecksichtigen
        try:
            typ = (anschluss / "type").read_text().strip()
            if typ != "1":
                continue

            geraet = (anschluss / "device")
            treiber = (geraet / "driver").resolve().name

            status = (anschluss / "carrier").read_text().strip()
            kabel = "Verbunden" if status == "1" else "Nicht verbunden"

        except (OSError, ValueError):
            continue

        gefunden += 1
        ergebnis = subprocess.run(
            ["ip", "-4", "-o", "addr", "show", "dev", anschluss.name],
            capture_output=True,
            text=True
        )

        ip_adressen = []
        if ergebnis.returncode == 0:
            for zeile in ergebnis.stdout.splitlines():
                teile = zeile.split()
                if "inet" in teile:
                    ip_adressen.append(teile[teile.index("inet") + 1])

        print(f"Anschluss: {anschluss.name}")
        print(f"Treiber: {treiber}")
        print(f"Netzwerkkabel: {kabel}")
        print("IPv4-Adressen:",
              ", ".join(ip_adressen) if ip_adressen else "Keine")
        print("----------------------------------------")
        

    if gefunden == 0:
        print("Keine physischen Ethernet-Anschluesse gefunden.")


if __name__ == "__main__":
    netzwerkanschluesse_suchen()

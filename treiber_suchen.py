#!/usr/bin/env python3

import subprocess


def treiber_suchen():
    print("========================================")
    print(" Linux Druckerassistent 1.0 Beta")
    print(" Verfügbare Druckertreiber suchen")
    print("========================================")
    print()

    print("Prüfe lokal verfügbare Druckertreiber ...")

    ergebnis = subprocess.run(
        ["lpinfo", "-m"],
        capture_output=True,
        text=True
    )

    if ergebnis.returncode != 0:
        print("Die Druckertreiber konnten nicht abgefragt werden.")
        return

    treiber = ergebnis.stdout.splitlines()

    print(f"Gefundene Treibereinträge: {len(treiber)}")
    print()
    print("Es wurden keine Treiber heruntergeladen oder installiert.")


if __name__ == "__main__":
    treiber_suchen()

#!/usr/bin/env python3

import subprocess


def vorhandene_drucker_suchen():
    print("========================================")
    print(" Linux Druckerassistent 1.0 Beta")
    print(" Bereits eingerichtete Drucker")
    print("========================================")
    print()

    ergebnis = subprocess.run(
        ["lpstat", "-v"],
        capture_output=True,
        text=True
    )

    if ergebnis.returncode != 0:
        print("Vorhandene Drucker konnten nicht abgefragt werden.")
        return

    if not ergebnis.stdout.strip():
        print("Keine eingerichteten Drucker gefunden.")
        return

    print(ergebnis.stdout.strip())
    print()
    print("Es wurden keine Druckereinstellungen verändert.")


if __name__ == "__main__":
    vorhandene_drucker_suchen()

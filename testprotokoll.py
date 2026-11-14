#!/usr/bin/env python3

import subprocess
import sys
from datetime import datetime
from pathlib import Path


def testprotokoll_erstellen():
    projektordner = Path(__file__).resolve().parent
    hauptprogramm = projektordner / "druckerassistent.py"

    zeitstempel = datetime.now().strftime("%Y%m%d-%H%M%S")
    protokolldatei = projektordner / f"testprotokoll-{zeitstempel}.txt"

    print("Linux-Druckerassistent 1.0 Beta")
    print("Testprotokoll wird erstellt ...")

    if not hauptprogramm.is_file():
        print("Fehler: Hauptprogramm nicht gefunden.")
        return

    with protokolldatei.open("w", encoding="utf-8") as datei:
        ergebnis = subprocess.run(
            [sys.executable, "-u", str(hauptprogramm)],
            stdout=datei,
            stderr=subprocess.STDOUT,
            check=False
        )

    print(f"Testprotokoll gespeichert: {protokolldatei}")

    if ergebnis.returncode != 0:
        print(f"Das Hauptprogramm meldete Fehlercode {ergebnis.returncode}.")

    print("WICHTIG: Vor der Weitergabe persönliche Daten,")
    print("IP-Adressen und Geräteinformationen überprüfen.")


if __name__ == "__main__":
    testprotokoll_erstellen()

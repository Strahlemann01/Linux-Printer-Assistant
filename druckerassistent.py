#!/usr/bin/env python3

import subprocess
from pathlib import Path

PROJEKTORDNER = Path(__file__).resolve().parent
ERKENNUNG = PROJEKTORDNER / "erkennung"


def baustein_starten(dateiname):
    datei = ERKENNUNG / dateiname

    if not datei.is_file():
        print(f"Fehler: {dateiname} wurde nicht gefunden.")
        return

    ergebnis = subprocess.run(
        ["python3", str(datei)],
        check=False
    )

    if ergebnis.returncode != 0:
        print(f"Fehler beim Ausführen von {dateiname}.")


def main():
    print("========================================")
    print(" Universeller Linux Druckerassistent 1.0")
    print(" Linux Mint und Ubuntu")
    print("========================================")
    
    print()
    print("0. Systemvoraussetzungen überprüfen")
    subprocess.run(["python3", str(PROJEKTORDNER / "voraussetzungen_pruefen.py")], check=False)

    print()
    print("1. Netzwerkanschlüsse überprüfen")
    baustein_starten("netzwerkanschluesse.py")

    print()
    print("2. Netzwerkbereiche ermitteln")
    baustein_starten("netzwerkbereiche.py")

    print()
    print("3. Verfügbare Drucker erkennen")
    baustein_starten("drucker_suchen.py")

    print()
    print("4. IPP- und Avahi-Druckdienste suchen")
    baustein_starten("druckdienste.py")

    print()
    print("5. Netzwerkdrucker und Modelle suchen")
    baustein_starten("netzwerkdrucker_suchen.py")

    print()
    print("6. Druckerergebnisse zusammenführen")
    baustein_starten("drucker_zusammenfuehren.py")

    print()
    print("7. USB-Drucker suchen")
    baustein_starten("usb_drucker_suchen.py")

    print()
    print("8. Bereits eingerichtete Drucker erkennen")
    subprocess.run(["python3", str(PROJEKTORDNER / "vorhandene_drucker.py")], check=False)

    print()
    print("9. Lokal verfügbare Druckertreiber suchen")
    subprocess.run(["python3", str(PROJEKTORDNER / "treiber_suchen.py")], check=False)

    print()
    print("Erkennung abgeschlossen.")
    print("Es wurden keine Druckereinstellungen verändert.")

if __name__ == "__main__":
    main()

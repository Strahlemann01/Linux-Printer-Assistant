#!/usr/bin/env python3

import subprocess
from pathlib import Path


def linux_usb_drucker_suchen():
    print("Suche USB-Drucker direkt über Linux ...")

    usb_pfad = Path("/sys/bus/usb/devices")

    if not usb_pfad.is_dir():
        print("USB-Geräteinformationen nicht verfügbar.")
        return

    for geraet in usb_pfad.iterdir():
        klasse_datei = geraet / "bInterfaceClass"

        if not klasse_datei.is_file():
            continue

        klasse = klasse_datei.read_text().strip()

        if klasse == "07":
            print(f"USB-Druckerschnittstelle gefunden: {geraet.name}")
            hersteller_datei = geraet.parent / "manufacturer"
            if hersteller_datei.is_file():
                print(f"Hersteller: {hersteller_datei.read_text().strip()}")
            modell_datei = geraet.parent / "product"
            if modell_datei.is_file():
                print(f"Modell: {modell_datei.read_text().strip()}")

def usb_drucker_suchen():
    print("========================================")
    print(" Linux Druckerassistent 1.0")
    print(" USB-Drucker suchen")
    print("========================================")
    print()

    ergebnis = subprocess.run(
        ["lpinfo", "-v"],
        capture_output=True,
        text=True
    )

    if ergebnis.returncode != 0:
        print("Fehler bei der USB-Druckersuche.")
        return

    gefunden = []

    for zeile in ergebnis.stdout.splitlines():
        teile = zeile.split(maxsplit=1)

        if len(teile) != 2:
            continue

        typ, adresse = teile

        if typ == "direct" and adresse.startswith("usb://"):
            gefunden.append(adresse)

    if gefunden:
        for nummer, adresse in enumerate(gefunden, start=1):
            print(f"USB-Drucker {nummer}")
            print(f"Adresse: {adresse}")
            print("----------------------------------------")
    else:
        print("Momentan kein USB-Drucker über CUPS erkannt.")

    print()
    print("Es wurden keine Druckereinstellungen verändert.")


if __name__ == "__main__":
    usb_drucker_suchen()
    linux_usb_drucker_suchen()

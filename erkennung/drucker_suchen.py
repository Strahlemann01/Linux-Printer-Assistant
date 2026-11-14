#!/usr/bin/env python3

import subprocess


def drucker_suchen():
    print("========================================")
    print(" Linux Druckerassistent 1.0")
    print(" Automatische Druckererkennung")
    print("========================================")
    print()

    ergebnis = subprocess.run(
        ["lpinfo", "-l", "-v"],
        capture_output=True,
        text=True
    )

    if ergebnis.returncode != 0:
        print("Fehler: CUPS-Druckererkennung fehlgeschlagen.")
        return

    drucker = []

    for block in ergebnis.stdout.split("Gerät:"):
        if "URI = " not in block:
            continue

        daten = {}

        for zeile in block.splitlines():
            zeile = zeile.strip()

            if " = " in zeile:
                schluessel, wert = zeile.split(" = ", 1)
                daten[schluessel] = wert

        uri = daten.get("URI", "")

        # Nur konkrete Druckerverbindungen anzeigen
        if "://" not in uri:
            continue

        drucker.append(daten)

    if not drucker:
        print("Keine Drucker automatisch gefunden.")
        return

    for nummer, eintrag in enumerate(drucker, start=1):
        print(f"Drucker {nummer}")
        print("Hersteller/Modell:",
              eintrag.get("Hersteller-und-Modell", "Unbekannt"))
        print("Verbindung:", eintrag.get("Klasse", "Unbekannt"))
        print("Adresse:", eintrag.get("URI", "Unbekannt"))
        print("Geräte-ID:", eintrag.get("Geräte-ID", ""))
        print("----------------------------------------")


if __name__ == "__main__":
    drucker_suchen()

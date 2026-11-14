#!/usr/bin/env python3
import re
import subprocess
from urllib.parse import urlparse
def cups_drucker_abfragen():
    ergebnis = subprocess.run(
        ["lpinfo", "-v"],
        capture_output=True,
        text=True
    )

    if ergebnis.returncode != 0:
        return []

    return [
        zeile.split()[-1]
        for zeile in ergebnis.stdout.splitlines()
        if "://" in zeile
    ]


def snmp_modell_abfragen(adresse):
    try:
        ergebnis = subprocess.run(
            [
                "snmpget", "-v", "2c", "-c", "public",
                "-Oqv", "-t", "1", "-r", "0",
                adresse, "1.3.6.1.2.1.25.3.2.1.3.1"
            ],
            capture_output=True,
            text=True,
            timeout=3
        )

        if ergebnis.returncode == 0:
            return ergebnis.stdout.strip().strip('"')

    except (OSError, subprocess.TimeoutExpired):
        pass

    return ""


def adresse_aus_uri(uri):
    parsed = urlparse(uri)

    if parsed.scheme not in ("socket", "ipp", "ipps", "http", "https", "lpd"):
        return None

    return parsed.hostname


def drucker_hinzufuegen(drucker, adresse, modell, quelle):
    if adresse not in drucker:
        drucker[adresse] = {
            "adresse": adresse,
            "modell": modell,
            "quellen": [quelle]
        }
    else:
        if quelle not in drucker[adresse]["quellen"]:
            drucker[adresse]["quellen"].append(quelle)

        if not drucker[adresse]["modell"] and modell:
            drucker[adresse]["modell"] = modell


def drucker_zusammenfuehren():
    print("========================================")
    print(" Linux Druckerassistent 1.0")
    print(" Druckerergebnisse zusammenfuehren")
    print("========================================")
    print()

    drucker = {}

    for uri in cups_drucker_abfragen():
        adresse = adresse_aus_uri(uri)

        if adresse:
            drucker_hinzufuegen(
                drucker, adresse, "", "CUPS"
            )

            modell = snmp_modell_abfragen(adresse)

            if modell:
                drucker_hinzufuegen(
                    drucker, adresse, modell, "SNMP"
                )
    

    print("Vorbereitung der gemeinsamen Druckerliste.")
    print(f"Aktuell zusammengefuehrte Drucker: {len(drucker)}")

    print()

    for eintrag in drucker.values():
        print(f"IP-Adresse: {eintrag['adresse']}")
        print(f"Druckermodell: {eintrag['modell'] or 'Unbekannt'}")
        print(f"Erkennungsmethoden: {', '.join(eintrag['quellen'])}")
        print("----------------------------------------")



if __name__ == "__main__":
    drucker_zusammenfuehren()

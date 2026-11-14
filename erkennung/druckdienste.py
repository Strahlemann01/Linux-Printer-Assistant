#!/usr/bin/env python3

import shutil
import subprocess


def druckdienste_suchen():
    print("========================================")
    print(" Linux Druckerassistent 1.0")
    print(" IPP- und DNS-SD-Druckersuche")
    print("========================================")
    print()

    # IPP-Druckdienste suchen
    if shutil.which("ippfind"):
        print("Suche nach IPP-Druckdiensten ...")

        ergebnis = subprocess.run(
            ["ippfind", "-T", "5"],
            capture_output=True,
            text=True,
            timeout=10
        )

        if ergebnis.stdout.strip():
            print(ergebnis.stdout.strip())
        else:
            print("Keine IPP-Druckdienste gefunden.")
    else:
        print("ippfind ist nicht installiert.")

    print()

    # Weitere Druckdienste ueber Avahi suchen
    if shutil.which("avahi-browse"):
        print("Suche nach DNS-SD-Druckdiensten ...")

        diensttypen = [
            "_ipp._tcp",
            "_ipps._tcp",
            "_printer._tcp",
            "_pdl-datastream._tcp"
        ]

        gefunden = set()

        for dienst in diensttypen:
            try:
                ergebnis = subprocess.run(
                    ["avahi-browse", "-rt", dienst],
                    capture_output=True,
                    text=True,
                    timeout=8
                )

                for zeile in ergebnis.stdout.splitlines():
                    if zeile.startswith("="):
                        gefunden.add(zeile.strip())

            except subprocess.TimeoutExpired:
                continue

        if gefunden:
            for eintrag in sorted(gefunden):
                print(eintrag)
        else:
            print("Keine DNS-SD-Druckdienste gefunden.")
    else:
        print("avahi-browse ist nicht installiert.")

    print()
    print("Druckdienstsuche abgeschlossen.")


if __name__ == "__main__":
    druckdienste_suchen()

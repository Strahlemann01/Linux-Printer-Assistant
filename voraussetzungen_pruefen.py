#!/usr/bin/env python3

import shutil


def voraussetzungen_pruefen():
    print("========================================")
    print(" Linux Druckerassistent 1.0 Beta")
    print(" Systemvoraussetzungen überprüfen")
    print("========================================")
    print()

    programme = [
        "python3",
        "lpinfo",
        "lpstat",
        "ip",
        "ippfind",
        "avahi-browse",
        "snmpget"
    ]

    fehlende_programme = []

    for programm in programme:
        if shutil.which(programm):
            print(f"{programm}: vorhanden")
        else:
            print(f"{programm}: FEHLT")
            fehlende_programme.append(programm)

    print()

    if fehlende_programme:
        print("ACHTUNG: Es fehlen benötigte Programme.")
        print("Einige Erkennungsfunktionen funktionieren")
        print("möglicherweise nicht vollständig.")
    else:
        print("Alle überprüften Programme sind vorhanden.")

    print()
    print("Es wurden keine Systemeinstellungen verändert.")


if __name__ == "__main__":
    voraussetzungen_pruefen()

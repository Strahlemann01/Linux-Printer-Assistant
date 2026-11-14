#!/usr/bin/env python3

import ipaddress
import json
import subprocess
from pathlib import Path


def netzwerkbereiche_suchen():
    print("========================================")
    print(" Linux Druckerassistent 1.0")
    print(" Physische IPv4-Netzwerke")
    print("========================================")
    print()

    ergebnis = subprocess.run(
        ["ip", "-j", "-4", "route", "show", "scope", "link"],
        capture_output=True,
        text=True
    )

    if ergebnis.returncode != 0:
        print("Fehler: Netzwerkbereiche konnten nicht gelesen werden.")
        return

    gefunden = set()

    for route in json.loads(ergebnis.stdout):
        anschluss = route.get("dev", "")
        ziel = route.get("dst", "")

        # Nur physische Netzwerkanschluesse verwenden
        if not (Path("/sys/class/net") / anschluss / "device").exists():
            continue

        try:
            netz = ipaddress.ip_network(ziel, strict=False)
        except ValueError:
            continue

        if netz.version != 4:
            continue

        gefunden.add((str(netz), anschluss))

    if not gefunden:
        print("Keine physischen IPv4-Netzwerke gefunden.")
        return

    for netz, anschluss in sorted(gefunden):
        print(f"Netzwerk: {netz}")
        print(f"Anschluss: {anschluss}")
        print("----------------------------------------")


if __name__ == "__main__":
    netzwerkbereiche_suchen()

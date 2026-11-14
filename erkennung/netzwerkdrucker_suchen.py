#!/usr/bin/env python3

import concurrent.futures
import ipaddress
import json
import socket
import subprocess
import shutil
from pathlib import Path



def netzwerkdrucker_suchen():
    print("========================================")
    print(" Linux Druckerassistent 1.0")
    print(" Netzwerkdrucker suchen")
    print("========================================")
    print()

    ergebnis = subprocess.run(
        ["ip", "-j", "-4", "route", "show", "scope", "link"],
        capture_output=True,
        text=True
    )

    if ergebnis.returncode != 0:
        print("Fehler beim Ermitteln der Netzwerke.")
        return

    netzwerke = set()

    for route in json.loads(ergebnis.stdout):
        anschluss = route.get("dev", "")
        ziel = route.get("dst", "")

        if not (Path("/sys/class/net") / anschluss / "device").exists():
            continue

        try:
            netz = ipaddress.ip_network(ziel, strict=False)
        except ValueError:
            continue

        # Nur kleine IPv4-Netzwerke automatisch pruefen
        if netz.version == 4 and netz.num_addresses <= 256:
            netzwerke.add(netz)

    if not netzwerke:
        print("Kein geeignetes Netzwerk gefunden.")
        return
    def modell_abfragen(ip):
        if not shutil.which("snmpget"):
            return "SNMP nicht verfügbar"

        try:
            ergebnis = subprocess.run(
                [
                    "snmpget", "-v", "2c", "-c", "public",
                    "-Oqv", "-t", "1", "-r", "0",
                    str(ip), "1.3.6.1.2.1.25.3.2.1.3.1"
                ],
                capture_output=True,
                text=True,
                timeout=3
            )

            if ergebnis.returncode == 0:
                return ergebnis.stdout.strip().strip('"')

        except (OSError, subprocess.TimeoutExpired):
            pass

        return "Modell unbekannt"


    def pruefen(ip):
        try:
            with socket.create_connection((str(ip), 9100), timeout=1):
                return str(ip)
        except (OSError, TimeoutError):
            return None

    gefunden = set()

    for netz in sorted(netzwerke):
        print(f"Durchsuche Netzwerk: {netz}", flush=True)

        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
            for adresse in pool.map(pruefen, netz.hosts()):
                if adresse:
                    gefunden.add(adresse)

    print()

    if gefunden:
        for adresse in sorted(gefunden):
            modell = modell_abfragen(adresse)
            print(f"Moeglicher Drucker: {adresse}")
            print(f"Modell laut SNMP: {modell}")
            print("Port 9100 erreichbar")
            print("----------------------------------------")
    else:
        print("Keine Geraete mit offenem Druckerport gefunden.")

    print()
    print("Hinweis: Ein offener Port beweist noch nicht,")
    print("dass das Geraet tatsaechlich ein Drucker ist.")


if __name__ == "__main__":
    netzwerkdrucker_suchen()

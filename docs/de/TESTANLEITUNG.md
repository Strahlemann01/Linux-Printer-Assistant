# Linux Printer Assistant 1.0 Beta
## Deutsche Testanleitung

### 1. Ziel des Programms

Linux Printer Assistant ist ein experimentelles Programm zur Erkennung und Diagnose von Druckern unter Linux Mint und Ubuntu.

Wir suchen freiwillige Tester und Entwickler, die das Programm auf Fehler, Kompatibilität und Verbesserungsmöglichkeiten überprüfen.

**Besonders wichtig ist die USB-Druckererkennung, da diese bisher nicht mit einem tatsächlich angeschlossenen USB-Drucker getestet wurde.**

### 2. Systemvoraussetzungen

- Linux Mint oder Ubuntu
- Python 3
- CUPS (`lpinfo`, `lpstat`)
- iproute2 (`ip`)
- IPP-Werkzeuge (`ippfind`)
- Avahi-Werkzeuge (`avahi-browse`)
- SNMP-Werkzeuge (`snmpget`)

Fehlende Programme können einzelne Funktionen beeinträchtigen.

### 3. Installation und Programmstart

Diese Anleitung richtet sich an erfahrene Linux-Anwender,
Tester und Entwickler.

Getestete Entwicklungsumgebung: Linux Mint 22.3.

#### Benötigte Systemwerkzeuge installieren

```bash
sudo apt update
sudo apt install git python3 cups-client cups-ipp-utils iproute2 avahi-utils snmp
```

Ein funktionierendes CUPS-System wird vorausgesetzt.

#### Projekt herunterladen

```bash
git clone https://github.com/Strahlemann01/Linux-Printer-Assistant.git
cd Linux-Printer-Assistant
```

#### Druckerassistent starten

```bash
python3 druckerassistent.py
```

#### Diagnoseprotokoll erstellen

```bash
python3 testprotokoll.py
```

#### Hinweise

Linux Printer Assistant 1.0 Beta ist eine experimentelle
Software zur Druckererkennung und Fehlerdiagnose.

Eine automatische Installation von Druckertreibern
ist noch nicht implementiert.

Die Software befindet sich in der Testphase.
Fehlerberichte und Verbesserungsvorschläge
sind ausdrücklich willkommen.

Bitte Diagnoseprotokolle vor einer Veröffentlichung
auf vertrauliche Informationen überprüfen.

### 4. USB-Drucker testen

1. Einen USB-Drucker anschließen.
2. Linux Printer Assistant starten.
3. Überprüfen, ob CUPS den Drucker erkennt.
4. Überprüfen, ob die Linux-USB-Erkennung den Drucker findet.
5. Hersteller und Modellbezeichnung kontrollieren.
6. Fehlermeldungen oder falsche Ergebnisse dokumentieren.

Bitte das Programm auch ohne angeschlossenen USB-Drucker testen.

### 5. Netzwerkdrucker testen

- Drucker über LAN oder WLAN verbinden.
- Erkannte IP-Adressen und Druckermodelle überprüfen.
- Die Erkennung über CUPS, SNMP, IPP und DNS-SD testen.
- Fehlende oder falsch erkannte Drucker melden.

### 6. Bereits eingerichtete Drucker

Überprüfen, ob vorhandene Druckerwarteschlangen korrekt angezeigt werden.

Bestehende Druckereinstellungen dürfen nicht ohne ausdrückliche Zustimmung verändert werden.

### 7. Bekannte Einschränkungen

- Die USB-Erkennung wurde noch nicht mit einem echten USB-Drucker getestet.
- Direkte Ethernet-Verbindungen ohne konfigurierte IP-Adresse werden möglicherweise nicht erkannt.
- Die Netzwerksuche unterstützt noch nicht alle Netzwerkkonfigurationen.
- Ein offener TCP-Port 9100 beweist nicht, dass ein Gerät tatsächlich ein Drucker ist.
- Eine automatische Internetsuche nach Druckertreibern ist noch nicht implementiert.
- Treiber können noch nicht automatisch heruntergeladen oder installiert werden.
- Die Bedienung erfolgt derzeit über das Terminal.
- Die Kompatibilität mit weiteren Linux-Distributionen ist noch ungeprüft.

### 8. Fehler melden

Bitte Fehler über **GitHub Issues** melden und möglichst folgende Informationen angeben:

- Linux-Distribution und Version
- Druckerhersteller und Modell
- Verbindung: USB, LAN oder WLAN
- Erwartetes Verhalten
- Tatsächliches Verhalten
- Vollständige Fehlermeldungen
- Schritte, mit denen sich der Fehler wiederholen lässt

**Datenschutz:** Bitte vor der Veröffentlichung von Testprotokollen Benutzernamen, Passwörter, private IP-Adressen, Gerätekennungen und andere vertrauliche Informationen entfernen.

### 9. Bisherige Testergebnisse

Das Programm wurde bisher unter Linux Mint 22.3 mit einem Kyocera FS-1061DN als Netzwerkdrucker getestet.

Der Drucker wurde über CUPS und SNMP erkannt.

Eine bereits eingerichtete Druckerwarteschlange konnte ebenfalls erkannt werden.

Die lokale CUPS-Abfrage lieferte auf dem Entwicklungsrechner 20.075 Treibereinträge.

Diese Ergebnisse garantieren nicht, dass sämtliche Drucker oder Linux-Systeme unterstützt werden.

### 10. Rückmeldungen

Wir freuen uns über Fehlerberichte, Verbesserungsvorschläge und technische Unterstützung über GitHub Issues.

Vielen Dank für eure Hilfe!

**Andreas Strahlendorf**  
Projektentwickler

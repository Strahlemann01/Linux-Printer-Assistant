# Linux Printer Assistant 1.0 Beta

## Druckertreiberquellen

### Ziel

Dieses Dokument enthält vertrauenswürdige Internetadressen, über die Linux-Druckertreiber und Informationen zur Druckerkompatibilität gefunden werden können.

**Wichtig:** Die aktuelle Beta-Version sucht noch nicht automatisch im Internet, lädt keine Treiber herunter und installiert keine Treiber. Diese Funktionen sind für spätere Versionen geplant.

## Offizielle Treiber- und Supportquellen

| Quelle | Internetadresse |
|---|---|
| Ubuntu-Paketquellen | https://packages.ubuntu.com/ |
| OpenPrinting | https://openprinting.github.io/ |
| HP – HPLIP | https://developers.hp.com/hp-linux-imaging-and-printing |
| Brother Support | https://support.brother.com/ |
| Canon Support | https://www.canon-europe.com/support/ |
| Epson Treiberdownloads | https://download.ebz.epson.net/dsc/search/01/search/ |
| Kyocera Support | https://www.kyoceradocumentsolutions.de/de/support/downloads.html |

Diese Webseiten dienen als Ausgangspunkt für die Treibersuche. Sie sind keine direkten Download-Adressen für bestimmte Druckertreiber.

## Geplanter Ablauf der Treibersuche

1. Druckerhersteller und genaue Modellbezeichnung erkennen.
2. Prüfen, ob treiberloses Drucken, beispielsweise mit IPP Everywhere, möglich ist.
3. Lokal verfügbare CUPS-Treibereinträge untersuchen.
4. Offizielle Paketquellen der Linux-Distribution durchsuchen.
5. OpenPrinting zur Kompatibilitätsprüfung heranziehen.
6. Falls erforderlich, die offizielle Supportseite des Herstellers prüfen.
7. Sicherstellen, dass der Treiber zum Drucker und Betriebssystem passt.
8. Gefundene Treiber und Bezugsquellen anzeigen.
9. Vor dem Herunterladen und Installieren die ausdrückliche Zustimmung des Benutzers einholen.

## Sicherheitsregeln

- Keine Treiber ohne Zustimmung installieren.
- Vorhandene Druckereinstellungen nicht ungefragt verändern.
- Vertrauenswürdige Paketquellen und offizielle Herstellerseiten bevorzugen.
- Heruntergeladene Dateien und deren Kompatibilität überprüfen.
- Keine unbekannten Installationsskripte ungeprüft ausführen.
- Keine vertraulichen Benutzerdaten sammeln oder veröffentlichen.

## Aktueller Entwicklungsstand

**Bereits vorhanden:**

- Druckererkennung über CUPS und weitere Verfahren
- Abfrage lokaler CUPS-Treibereinträge
- Erkennung bereits eingerichteter Drucker
- Prüfung der Systemvoraussetzungen

**Noch nicht vorhanden:**

- Automatische Internetsuche nach Druckertreibern
- Zuverlässige automatische Treiber-Kompatibilitätsprüfung
- Automatisches Herunterladen von Treibern
- Installation von Druckertreibern
- Benutzerabfrage vor einer Installation

## Tests und Mitarbeit

Linux-Entwickler und Druckerspezialisten sind eingeladen, die vorgesehenen Treiberquellen zu überprüfen und Verbesserungen vorzuschlagen.

Rückmeldungen können über **GitHub Issues** erfolgen.

**Projekt:** Linux Printer Assistant 1.0 Beta

**Projektentwickler:** Andreas Strahlendorf

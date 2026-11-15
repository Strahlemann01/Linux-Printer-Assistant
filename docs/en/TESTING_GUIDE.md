# Linux Printer Assistant 1.0 Beta
## Testing Guide

### 1. Purpose

Linux Printer Assistant is an experimental printer detection and diagnostic tool for Linux Mint and Ubuntu.

We are looking for volunteer testers and developers to identify bugs, evaluate compatibility, and suggest improvements.

**USB printer testing is especially important because this functionality has not yet been tested with a physically connected USB printer.**

### 2. Requirements

- Linux Mint or Ubuntu
- Python 3
- CUPS (`lpinfo`, `lpstat`)
- iproute2 (`ip`)
- IPP utilities (`ippfind`)
- Avahi utilities (`avahi-browse`)
- SNMP utilities (`snmpget`)

Some features may not work if required utilities are missing.

### 3. Running the Application

Download or clone the repository.

Open a terminal in the project directory and run:

`python3 druckerassistent.py`

To generate a diagnostic log, run:

`python3 testprotokoll.py`

### 4. USB Printer Tests

1. Connect a USB printer.
2. Start Linux Printer Assistant.
3. Check whether the printer is detected through CUPS.
4. Check whether Linux USB interface detection identifies the printer.
5. Verify the manufacturer and model information.
6. Record any errors or incorrect results.

Also test the application without a USB printer connected.

### 5. Network Printer Tests

- Test printers connected through Ethernet or Wi-Fi.
- Verify detected IP addresses and printer models.
- Check CUPS, SNMP, IPP and DNS-SD discovery.
- Report missing printers or incorrect identification.

### 6. Existing Printer Configurations

Verify that already configured printers are listed correctly.

The application must not modify existing printer configurations without user approval.

### 7. Known Limitations

- USB detection has not been verified with a real USB printer.
- Direct Ethernet connections without an assigned IP address may not be detected.
- Network discovery does not cover every network configuration.
- An open TCP port 9100 does not prove that a device is a printer.
- Automatic online driver searches are not implemented.
- Driver downloading and installation are not implemented.
- The current interface is terminal-based.
- Compatibility with other Linux distributions has not been established.

### 8. Reporting Problems

Please use GitHub Issues to report:

- Linux distribution and version
- Printer manufacturer and model
- Connection type (USB, Ethernet or Wi-Fi)
- Expected and actual behavior
- Error messages
- Steps to reproduce the problem

**Privacy:** Remove usernames, passwords, private IP addresses, device identifiers, and other confidential information from diagnostic logs before publishing them.

### 9. Current Test Status

The project has been tested on Linux Mint 22.3 with a Kyocera FS-1061DN network printer.

CUPS and SNMP identified the printer.

The existing printer queue was detected successfully.

The local CUPS driver query returned 20,075 entries on the development system.

These results do not guarantee compatibility with other printers or systems.

### 10. Feedback

Feedback, bug reports and technical suggestions are welcome through GitHub Issues.

Thank you for helping test Linux Printer Assistant!

**Andreas Strahlendorf**  
Project maintainer

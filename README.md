# Linux-Printer-Assistant
An experimental Linux printer detection and diagnostic tool for Linux Mint and Ubuntu, supporting USB and network printer discovery. Beta version – testers and developers welcome.
# Linux Printer Assistant 1.0 Beta

**A printer detection and diagnostic tool for Linux Mint and Ubuntu.**

Linux Printer Assistant is an experimental Python project intended to help users discover USB and network printers, identify available driver information, and diagnose printer configuration issues.

## Current Features

- Detection of physical network interfaces and IPv4 networks
- Network printer discovery using CUPS and SNMP
- Discovery of IPP and DNS-SD printing services
- USB printer detection using CUPS and Linux USB device information
- Identification of printer manufacturers and models when available
- Detection of existing CUPS printer queues
- Listing of locally available CUPS driver entries
- System dependency checks
- Diagnostic log generation

## Current Development Status

**This is a beta version for technical testing, not a finished printer installation tool.**

The project has been tested on Linux Mint 22.3 with a Kyocera FS-1061DN network printer.

USB detection has not yet been tested with a physically connected USB printer.

Automatic online driver searching, downloading, and installation are not yet implemented.

## Requirements

- Linux Mint or Ubuntu (other distributions have not been tested)
- Python 3
- CUPS utilities
- iproute2
- IPP utilities
- Avahi utilities
- SNMP utilities

Additional dependencies may be required.

## Running the Program

Open a terminal in the project directory and run:

```bash
python3 druckerassistent.py
```

To generate a diagnostic log:

```bash
python3 testprotokoll.py
```

Review diagnostic logs for private information before sharing them.

## Testing Help Wanted

We welcome feedback from Linux developers, printing specialists, and experienced users.

**USB printer testing is especially needed.**

We would appreciate help with:

- USB printers from different manufacturers
- Network printer discovery
- Driver identification
- Compatibility testing
- Error handling
- Python code review
- Security and reliability improvements

Please report any problems through GitHub Issues, including your Linux version, printer model, connection type, and steps to reproduce the problem.

Do not publish passwords, private network details, or other sensitive information.

## Safety

The current beta performs printer discovery and diagnostic checks. It does not install printer drivers or intentionally modify existing CUPS printer configurations.

Future driver installations are intended to require explicit user approval.

## AI Assistance

This project was initiated by a Linux Mint beginner with no programming experience and developed with the assistance of OpenAI ChatGPT.

The goal is to make printer detection and troubleshooting easier for Linux beginners.

## Project Contact
**Andreas Strahlendorf**

Feedback and contributions are welcome through this GitHub repository.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Documentation / Dokumentation

Documentation is available in English and German.

### English

- [Testing Guide](docs/en/TESTING_GUIDE.md)
- [Driver Sources](docs/en/DRIVER_SOURCES.md)

### Deutsch

- [Testanleitung](docs/de/TESTANLEITUNG.md)
- [Treiberquellen](docs/de/TREIBERQUELLEN.md)

### Testing Help Wanted

We welcome feedback from Linux developers and testers, especially those who can test physical USB printers.

USB detection has not yet been verified with a real USB printer.

Please report test results and suggestions through [GitHub Issues](https://github.com/Strahlemann01/Linux-Printer-Assistant/issues).

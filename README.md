Vaultora – File Encryption & Decryption Tool

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Vaultora is a secure file encryption and decryption tool built with Python and Flask. It uses Fernet (AES + HMAC) and PBKDF2 for password-based security. Supports all file types, works offline, and ensures data confidentiality with a simple, user-friendly interface.
Vaultora is a secure and lightweight file encryption and decryption tool built using Python and Flask. It allows users to protect sensitive data using password-based encryption with strong cryptographic standards.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Features

- 🔒 Encrypt and decrypt any file type (images, PDFs, text, etc.)
- 🔑 Password-based security
- 🧠 Secure key derivation using PBKDF2
- 🛡️ AES-based encryption via Fernet
- ⚡ Works completely offline
- 🧾 Preserves original file format after decryption
- 🎯 Simple and user-friendly interface

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tech Stack

- Python
- Flask
- Cryptography Library (Fernet, PBKDF2)
- HTML, CSS, JavaScript

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

How It Works

1. Upload any file
2. Enter a password
3. Choose:
   - Encrypt → returns encrypted `.txt` file  
   - Decrypt → restores original file  
4. Download the processed file

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Security Overview

- Uses :contentReference[oaicite:0]{index=0} for encryption (AES + HMAC)
- Uses :contentReference[oaicite:1]{index=1} for secure key generation
- Ensures:
  - Confidentiality (AES)
  - Integrity (HMAC)
  - Resistance to brute-force attacks (PBKDF2)
 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

File Structure:

vaultora-file-encryption/
│
├── app.py
├── crypto/
├── templates/
├── static/
├── uploads/
└── .venv/

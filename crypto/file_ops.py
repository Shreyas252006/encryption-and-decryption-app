from crypto.core import encrypt_data, decrypt_data
import os

import os

def encrypt_file(input_path, password):
    if not os.path.exists(input_path):
        raise FileNotFoundError("File does not exist")

    # Extract extension
    ext = os.path.splitext(input_path)[1]  #FileType: .jpeg, .txt, .pdf

    with open(input_path, "rb") as f:
        data = f.read()

    encrypted = encrypt_data(data, password)

    # Store extension + encrypted data
    combined = ext.encode() + b"||" + encrypted

    base = os.path.splitext(input_path)[0]
    output_path = base + ".txt"

    with open(output_path, "wb") as f:
        f.write(combined)

    return output_path


def decrypt_file(input_path, password):
    if not os.path.exists(input_path):
        raise FileNotFoundError("File does not exist")

    with open(input_path, "rb") as f:
        combined = f.read()

    # Split extension + encrypted data
    ext, encrypted = combined.split(b"||", 1)

    decrypted = decrypt_data(encrypted, password)

    # Restore original file
    base = os.path.splitext(input_path)[0]
    output_path = base + ext.decode()

    with open(output_path, "wb") as f:
        f.write(decrypted)

    return output_path
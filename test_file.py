from crypto.file_ops import encrypt_file, decrypt_file

file_path = ".venv\\ty.jpeg"

password = "Strong@123"

try:
    enc_file = encrypt_file(file_path, password)

    if not enc_file:
        raise Exception("Encryption failed")

    print("Encrypted file:", enc_file)

    dec_file = decrypt_file(enc_file, password)

    if not dec_file:
        raise Exception("Decryption failed")

    print("Decrypted file:", dec_file)

except Exception as e:
    print("Error:", e)
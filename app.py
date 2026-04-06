from flask import Flask, request, send_file, render_template
import os
from crypto.file_ops import encrypt_file, decrypt_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/encrypt", methods=["POST"])
def encrypt():
    try:
        file = request.files["file"]
        password = request.form["password"]

        if not file:
            return "No file uploaded", 400

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        print("Saved:", path)

        output = encrypt_file(path, password)

        print("Output:", output)

        if not output or not os.path.exists(output):
            return "Encryption failed", 500

        return send_file(output, as_attachment=True, download_name=os.path.basename(output))

    except Exception as e:
        print("ERROR:", e)
        return str(e), 500


@app.route("/decrypt", methods=["POST"])
def decrypt():
    try:
        # 🔹 Get file + password
        file = request.files.get("file")
        password = request.form.get("password")

        if not file or file.filename == "":
            return "No file uploaded", 400

        if not password:
            return "Password required", 400

        # 🔹 Save uploaded file
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        print("Saved file:", path)

        # 🔹 Decrypt
        output = decrypt_file(path, password)

        print("Decrypted output:", output)

        # 🔹 Validate output
        if not output or not os.path.exists(output):
            return "Decryption failed (file not created)", 500

        # 🔹 Send file with correct name
        return send_file(
            output,
            as_attachment=True,
            download_name=os.path.basename(output)
        )

    except Exception as e:
        print("ERROR during decryption:", e)
        return f"Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
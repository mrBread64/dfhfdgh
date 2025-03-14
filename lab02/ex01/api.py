from flask import Flask, request, jsonify
from cipher.playfair import PlayfairCipher
from cipher.caesar import CaesarCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigenereCipher
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

playfair_cipher = PlayfairCipher()
caesar_cipher = CaesarCipher()
railfence_cipher = RailFenceCipher()
vigenere_cipher = VigenereCipher()
rsa_cipher = RSACipher()
ecc_cipher = ECCCipher()

@app.route("/", methods=["GET"])
def home():
    data = request.json
    return jsonify({"message": "POST request received", "data": data})

# Playfair Cipher Routes
@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    data = request.json
    key = str(data['key'])
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = str(data['key'])
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = str(data['key'])
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_message': decrypted_text})

# Caesar Cipher Routes
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Rail Fence Cipher Routes
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Vigenere Cipher Routes
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = str(data['key'])
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = str(data['key'])
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# RSA Routes
@app.route("/api/rsa/generate_keys", methods=["POST"])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'RSA keys generated successfully'})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data['message']
    _, public_key = rsa_cipher.load_keys()
    encrypted_message = rsa_cipher.encrypt(message, public_key)
    return jsonify({'encrypted_message': encrypted_message.hex()})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext = bytes.fromhex(data['ciphertext'])
    private_key, _ = rsa_cipher.load_keys()
    decrypted_message = rsa_cipher.decrypt(ciphertext, private_key)
    return jsonify({'decrypted_message': decrypted_message})

# ECC Routes
@app.route("/api/ecc/generate_keys", methods=["POST"])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'ECC keys generated successfully'})

@app.route("/api/ecc/sign", methods=["POST"])
def ecc_sign():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    return jsonify({'signature': signature.hex()})

@app.route("/api/ecc/verify", methods=["POST"])
def ecc_verify():
    data = request.json
    message = data['message']
    signature = bytes.fromhex(data['signature'])
    _, public_key = ecc_cipher.load_keys()
    verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'verified': verified})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
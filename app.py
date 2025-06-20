from flask import Flask, request, jsonify

app = Flask(__name__)

# Store reservations in memory (temporary)
reservations = {}

@app.route('/set-reservation', methods=['POST'])
def set_reservation():
    data = request.get_json()
    device_id = data.get("device_id")
    if not device_id:
        return jsonify({"error": "device_id required"}), 400
    reservations[device_id] = {
        "start_time": data.get("start_time"),
        "end_time": data.get("end_time")
    }
    return jsonify({"status": "saved"})

@app.route('/get-reservation', methods=['GET'])
def get_reservation():
    device_id = request.args.get("device_id")
    if not device_id or device_id not in reservations:
        return jsonify({"error": "not found"}), 404
    return jsonify(reservations[device_id])

@app.route('/')
def hello():
    return "Reservation API is running."

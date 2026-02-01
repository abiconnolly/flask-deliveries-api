```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

def save_delivery(payload: dict) -> dict:
    """
    Simple in-memory 'save' stub to mimic persistence.
    In a real app, this would write to a database.
    """
    return {"id": str(uuid.uuid4()), **payload}

@app.route("/deliveries", methods=["POST"])
def create_delivery():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON payload"}), 400

    required_fields = ["route_id", "driver_name", "eta_minutes"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": "Missing required fields", "missing": missing}), 400

    route_id = data.get("route_id")
    driver_name = data.get("driver_name")
    eta_minutes = data.get("eta_minutes")
    notes = data.get("notes", "")

    # Validate route_id
    if not isinstance(route_id, str) or not route_id.strip():
        return jsonify({"error": "route_id must be a non-empty string"}), 400

    # Validate driver_name
    if not isinstance(driver_name, str) or not driver_name.strip():
        return jsonify({"error": "driver_name must be a non-empty string"}), 400
    if len(driver_name) > 50:
        return jsonify({"error": "driver_name must be 50 characters or fewer"}), 400

    # Validate eta_minutes
    if not isinstance(eta_minutes, int):
        return jsonify({"error": "eta_minutes must be an integer"}), 400
    if eta_minutes < 0:
        return jsonify({"error": "eta_minutes must be 0 or greater"}), 400

    # Validate notes (optional)
    if notes is None:
        notes = ""
    if not isinstance(notes, str):
        return jsonify({"error": "notes must be a string"}), 400
    if len(notes) > 280:
        return jsonify({"error": "notes must be 280 characters or fewer"}), 400

    saved = save_delivery({
        "route_id": route_id.strip(),
        "driver_name": driver_name.strip(),
        "eta_minutes": eta_minutes,
        "notes": notes.strip()
    })

    return jsonify({"data": saved}), 201

if __name__ == "__main__":
    app.run(debug=True)

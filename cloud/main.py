from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "status": "SevenHunter v20 Cloud Engine Running",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "version": "v20.0",
        "engine": {
            "elo": "active",
            "xg": "active",
            "odds_drift": "active",
            "squad_predictor": "v3",
            "manager_index": "v2",
            "national_mode": "on"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

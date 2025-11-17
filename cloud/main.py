from flask import Flask, request, jsonify
import datetime

# Import SevenHunter v20 Engine Modules
from engine.elo import calculate_elo
from engine.xg_projector import project_xg
from engine.odds_drift import analyze_odds_drift
from engine.motivation import evaluate_motivation
from engine.fatigue import calculate_fatigue
from engine.psychology import evaluate_psychology
from engine.squad_predictor import predict_squad
from engine.manager_index import evaluate_manager_style
from engine.national_mode import national_mode_adjust

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "status": "SevenHunter v20 Cloud Engine Running",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "available_modules": [
            "elo", "xg", "odds_drift", "motivation",
            "fatigue", "psychology", "squad_predictor",
            "manager_index", "national_mode"
        ]
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Calculate each engine module
    elo_res = calculate_elo(data["home_elo"], data["away_elo"])
    xg_res = project_xg(data["home_shots"], data["away_shots"])
    drift_res = analyze_odds_drift(
        data["open_home"], data["open_draw"], data["open_away"],
        data["live_home"], data["live_draw"], data["live_away"]
    )
    motivation_res = evaluate_motivation(data["motivation_home"], data["motivation_away"])
    fatigue_res = calculate_fatigue(data["minutes_last_game"], data["days_rest"])
    psych_res = evaluate_psychology(data["home_streak"], data["away_streak"])
    manager_res = evaluate_manager_style(
        data["attack_rate"], data["rotation_rate"], data["risk_rate"]
    )
    national_res = national_mode_adjust(
        data["home_advantage"], data["motivation_home"], data["motivation_away"],
        data["neutral_venue"], data["second_game"]
    )

    return jsonify({
        "elo": elo_res,
        "xg": xg_res,
        "odds_drift": drift_res,
        "motivation": motivation_res,
        "fatigue": fatigue_res,
        "psychology": psych_res,
        "manager": manager_res,
        "national_mode": national_res
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

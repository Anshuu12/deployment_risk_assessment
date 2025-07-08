from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict-risk", methods=["POST"])
def predict_risk():
    data = request.get_json()

    features = np.array([
        data.get("cpu_usage", 0),
        data.get("memory_usage", 0),
        data.get("error_rate", 0),
        data.get("response_time", 0)
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    risk_score = model.predict_proba(features)[0][1]

    return jsonify({
        "prediction": "High" if prediction == 1 else "Low",
        "risk_score": round(risk_score * 100, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)

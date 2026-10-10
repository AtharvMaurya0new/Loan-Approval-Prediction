import os
import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify
from utils import risk_analysis

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        d = request.get_json(force=True)

        dependents = int(d["dependents"])
        education = d["education"]
        selfemp = d["self_employed"]
        income = float(d["income"])
        loanamt = float(d["loan_amount"])
        loan_term = int(d["loan_term"])
        cibil = float(d["cibil"])

        res_assets = float(d["res_assets"])
        com_assets = float(d["com_assets"])
        lux_assets = float(d["lux_assets"])
        bank_assets = float(d["bank_assets"])

        if income <= 0:
            return jsonify(error="Annual income must be greater than 0."), 400

        # ---------- same code as before ----------
        data = pd.DataFrame([{
            "no_of_dependents": dependents,
            "education": 1 if education == "Graduate" else 0,
            "self_employed": 1 if selfemp == "Yes" else 0,
            "income_annum": income,
            "loan_amount": loanamt,
            "loan_term": loan_term,
            "cibil_score": cibil,
            "residential_assets_value": res_assets,
            "commercial_assets_value": com_assets,
            "luxury_assets_value": lux_assets,
            "bank_asset_value": bank_assets
        }])
        data["total_assets"] = (
            data["residential_assets_value"] +
            data["commercial_assets_value"] +
            data["luxury_assets_value"] +
            data["bank_asset_value"])

        data["loan_to_income"] = data["loan_amount"] / data["income_annum"]

        prediction = model.predict(data)
        prob = model.predict_proba(data)

        prediction = int(prediction[0])
        advice = risk_analysis(prediction, cibil, income, loanamt)
        # -----------------------------------------

        # colour level for the website (taken from your utils.py message)
        if advice.startswith("High"):
            level = "high"
        elif advice.startswith("Medium"):
            level = "medium"
        else:
            level = "low"

        return jsonify(
            approved=prediction == 1,
            probability=round(float(prob[0][1]) * 100, 1),
            loan_to_income=round(float(data["loan_to_income"][0]), 2),
            total_assets=float(data["total_assets"][0]),
            risk_level=level,
            advice=advice,
        )
    except (KeyError, ValueError, TypeError):
        return jsonify(error="Please fill in every field with valid numbers."), 400
    except Exception as e:
        return jsonify(error=f"Prediction failed: {e}"), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
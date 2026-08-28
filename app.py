import pandas as pd
import numpy as np
import pickle
import streamlit as st
from utils import risk_analysis

model=pickle.load(open("model.pkl","rb"))

st.title("LOAN APPROVED SYSTEM")

dependents=st.number_input("Dependent",0,10)
education=st.selectbox("education",["Graduate","Not Graduate"])
selfemp=st.selectbox("employed",["YES","NO"])
income=st.number_input("income")
loanamt=st.number_input("Loan Amount")
loan_term=st.number_input("time in Month",0,10)
cibil=st.number_input("cibil Score")

res_assets = st.number_input("Residential Assets")
com_assets = st.number_input("Commercial Assets")
lux_assets = st.number_input("Luxury Assets")
bank_assets = st.number_input("Bank Assets")

data=pd.DataFrame([{
    "no_of_dependents": dependents,
    "education": 1 if education=="Graduate" else 0,
    "self_employed": 1 if selfemp=="Yes" else 0,
    "income_annum": income,
    "loan_amount": loanamt,
    "loan_term": loan_term,
    "cibil_score": cibil,
    "residential_assets_value": res_assets,
    "commercial_assets_value": com_assets,
    "luxury_assets_value": lux_assets,
    "bank_asset_value": bank_assets
}])
data["total_assets"]=(
    data["residential_assets_value"]+
    data["commercial_assets_value"] +
    data["luxury_assets_value"] +
    data["bank_asset_value"])

data["loan_to_income"]=data["loan_amount"]/data["income_annum"]


if st.button("predict loan"):
    prediction = model.predict(data)
    prob = model.predict_proba(data)

    if prediction==1:
        st.success("loan Approved")
    else:
        st.error("loan rejected")

    advice=risk_analysis(prediction,cibil,income,loanamt)
    st.info(advice)        
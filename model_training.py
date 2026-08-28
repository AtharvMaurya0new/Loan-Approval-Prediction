import numpy as np
import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline

df = pd.read_csv("loan_approval_dataset.csv")

df.columns = df.columns.str.strip()

df = df.drop("loan_id", axis=1)

df["education"] = df["education"].str.strip().map({"Graduate":1, "Not Graduate":0})
df["self_employed"] = df["self_employed"].str.strip().map({"Yes":1, "No":0})
df["loan_status"] = df["loan_status"].str.strip().map({"Approved":1, "Rejected":0})

df["total_assets"] = (
    df["residential_assets_value"] +
    df["commercial_assets_value"] +
    df["luxury_assets_value"] +
    df["bank_asset_value"]
)

df["loan_to_income"] = df["loan_amount"] / df["income_annum"]

df.fillna(df.median(numeric_only=True), inplace=True)

X = df.drop("loan_status", axis=1)
y = df["loan_status"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


models = {
    "logistic": Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression())
    ]),
    
    "tree": Pipeline([
        ('scaler', StandardScaler()),
        ('model', DecisionTreeClassifier())
    ]),
    
    "forest": Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestClassifier())
    ])
}

best_score = 0
best_model = None

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    score = accuracy_score(y_test, pred)

    print(f"{name} Accuracy:", score)
    print(f"{name} classification", classification_report(y_test,pred))
    print(f"{name} confusion:", confusion_matrix(y_test,pred))

    if score > best_score:
        best_score = score
        best_model = model

print("\nBEST MODEL =", best_model)
y_prob=best_model.predict_proba(X_test)[:,1]
fpr,tpr,_=roc_curve(y_test,y_prob)

plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()

pickle.dump(best_model, open("model.pkl", "wb"))
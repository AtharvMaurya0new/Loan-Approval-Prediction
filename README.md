[Loan Approval Prediction](https://69wqufbehsgvmqbkapphmkm.streamlit.app/)
# 🏦 Loan Approval Prediction System

A machine learning-based application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant financial and demographic information.

The project includes data preprocessing, feature engineering, multiple machine learning models, model evaluation, and a Streamlit web interface for making predictions.

---

## 🚀 Features

- Data preprocessing and cleaning
- Categorical data encoding
- Feature engineering
- Loan-to-income ratio calculation
- Total asset calculation
- Multiple machine learning models
- Model comparison using accuracy
- Classification report and confusion matrix
- ROC curve analysis
- Streamlit-based prediction interface
- Basic loan risk analysis

---

## 🧠 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

The best-performing model based on test accuracy is automatically selected and saved as `model.pkl`.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Streamlit**
- **Pickle**

---

## 📊 Features Used

The model uses applicant information such as:

- Number of dependents
- Education
- Self-employment status
- Annual income
- Loan amount
- Loan term
- CIBIL score
- Residential asset value
- Commercial asset value
- Luxury asset value
- Bank asset value

### Feature Engineering

Two additional features are created:

```text
Total Assets = Residential Assets + Commercial Assets + Luxury Assets + Bank Assets

Loan-to-Income Ratio = Loan Amount / Annual Income

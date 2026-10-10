<div align="center">

# 🏦 LoanLens: Loan Approval Prediction System 💸

**Check your loan eligibility instantly with Machine Learning 🤖**

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Open_Website-0b6b4f?style=for-the-badge)](https://loan-approval-prediction-rouge-zeta.vercel.app)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-F7931E?logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.3-150458?logo=pandas&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployed_on-Vercel-000000?logo=vercel&logoColor=white)

### 👉 [Try it live: loan-approval-prediction-rouge-zeta.vercel.app](https://loan-approval-prediction-rouge-zeta.vercel.app)

</div>

---

## 📖 About the project

LoanLens is a full-stack machine learning website that predicts whether a loan application will be **Approved ✅** or **Rejected ❌** from the applicant's financial and personal details.

You enter your details, and the website instantly shows:

- 🔮 The **Approved / Rejected** prediction
- 📈 An animated **approval-chance gauge**
- 📊 **Loan-to-income** and **total assets** cards
- 🛡️ A colour-coded **risk analysis** (🟢 low, 🟡 medium, 🔴 high)

---

## ✨ Features

- 🧹 Data preprocessing and cleaning
- 🔤 Categorical data encoding
- 🛠️ Feature engineering (total assets and loan-to-income ratio)
- 🤖 Three machine learning models trained and compared
- 📉 Model evaluation with accuracy, classification report, confusion matrix and ROC curve
- 🌐 Responsive website that works on phones and laptops
- 🌙 Light and dark mode that follow your device
- ⚠️ Clear messages for missing or invalid inputs
- 🚀 Deployed on Vercel with every push to GitHub

---

## 🧠 Machine learning models

| Model | Purpose |
|---|---|
| Logistic Regression | Simple, fast baseline |
| Decision Tree Classifier | Rule-based decisions |
| Random Forest Classifier | Many trees combined for stronger results |

Each model is wrapped in a scikit-learn **Pipeline** with a `StandardScaler`, so scaling is applied automatically at prediction time. The model with the best test accuracy is selected and saved as `model.pkl`.

---

## 📋 Input features

| Feature | Description |
|---|---|
| 👨‍👩‍👧 Dependents | Number of dependents |
| 🎓 Education | Graduate or Not Graduate |
| 💼 Self employed | Yes or No |
| 💰 Annual income | In ₹ |
| 🏦 Loan amount | In ₹ |
| 📅 Loan term | In years |
| 📊 CIBIL score | 300 to 900 |
| 🏡 Residential assets | Value in ₹ |
| 🏢 Commercial assets | Value in ₹ |
| 💎 Luxury assets | Value in ₹ |
| 🏦 Bank assets | Value in ₹ |

### 🛠️ Engineered features

```text
Total Assets     = Residential + Commercial + Luxury + Bank Assets
Loan-to-Income   = Loan Amount / Annual Income
```

---

## 🧰 Tech stack

| Layer | Tools |
|---|---|
| 🎨 Frontend | HTML, CSS, JavaScript |
| ⚙️ Backend | Python, Flask |
| 🤖 Machine learning | scikit-learn, Pandas, NumPy |
| 📦 Model storage | Pickle |
| ☁️ Hosting | Vercel |
| 🔧 Version control | Git and GitHub |

---

## 🗂️ Project structure

```text
Loan-Approval-Prediction/
├── app.py                      # Flask app: serves the website and the /predict API
├── utils.py                    # Risk analysis logic
├── model_training.py           # Trains, compares and saves the best model
├── model.pkl                   # Trained model (scikit-learn pipeline)
├── loan_approval_dataset.csv   # Dataset
├── templates/
│   └── index.html              # Website page (HTML, CSS, JS)
├── requirements.txt            # Python dependencies
└── README.md
```

---

## ⚙️ How it works

```text
Browser form  ──►  Flask /predict  ──►  ML model  ──►  Result back to the browser
  (you type)         (app.py)        (model.pkl)     (gauge, verdict, risk analysis)
```

---

## ▶️ Run it on your computer

**1. Clone the repository**

```bash
git clone https://github.com/AtharvMaurya0new/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction
```

**2. Install the dependencies**

```bash
pip install -r requirements.txt
```

**3. Start the website**

```bash
python app.py
```

**4. Open it in your browser**

```text
http://localhost:5000
```

### 🔁 Retrain the model (optional)

```bash
python model_training.py
```

This creates a fresh `model.pkl`. Keep the scikit-learn version in `requirements.txt` the same as the one you trained with.

---

## ☁️ Deployment

The website is hosted on **Vercel**. Every push to the `main` branch redeploys it automatically.

🔗 **Live link:** https://loan-approval-prediction-rouge-zeta.vercel.app

---

## ⚠️ Disclaimer

This project is for **learning and demonstration only**. The prediction is a guide from a trained model and is **not** a real bank decision or financial advice.

---

## 👨‍💻 Author

**Atharv Maurya**
GitHub: [@AtharvMaurya0new](https://github.com/AtharvMaurya0new)

---

<div align="center">

⭐ If you like this project, please give it a star! ⭐

Made with ❤️ using Flask and scikit-learn

</div>

def risk_analysis(prediction, cibil, income, loanamt):
    if prediction == 0:
        if cibil < 600:
            return "High Risk: Rejected due to low CIBIL"
        return "High Risk: Loan Rejected"

    if cibil < 600:
        return "Medium Risk: Low CIBIL score"

    if loanamt > income:
        return "Medium Risk: Loan too high compared to income"

    return "Low Risk: Safe to approve"
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate EMI
def calculate_emi(loan_amount, tenure_years, interest_rate):
    tenure_months = tenure_years * 12
    monthly_interest_rate = (interest_rate / 100) / 12
    
    if monthly_interest_rate > 0:
        emi = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_months / ((1 + monthly_interest_rate) ** tenure_months - 1)
    else:
        emi = loan_amount / tenure_months

    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount

    return emi, total_payment, total_interest

@app.route('/', methods=['GET', 'POST'])
def emi_calculator():
    emi = None
    total_payment = None
    total_interest = None
    loan_amount = 1000000  # Default value
    tenure_years = 15      # Default value
    interest_rate = 7      # Default value

    if request.method == 'POST':
        loan_amount = float(request.form.get('loan_amount'))
        tenure_years = int(request.form.get('tenure_years'))
        interest_rate = float(request.form.get('interest_rate'))

        emi, total_payment, total_interest = calculate_emi(loan_amount, tenure_years, interest_rate)

    return render_template('emi_calculator.html', emi=emi, total_payment=total_payment, total_interest=total_interest, loan_amount=loan_amount, tenure_years=tenure_years, interest_rate=interest_rate)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

# SIP Calculation Function
def calculate_sip(P, i, n):
    M = P * (((1 + i) ** n - 1) / i) * (1 + i)
    return M

@app.route('/', methods=['GET', 'POST'])
def sip_calculator():
    P = 5000  # Default value
    i = 12    # Default value
    n = 10    # Default value
    M = None
    total_invested = None
    estimated_returns = None

    if request.method == 'POST':
        P = float(request.form.get('P'))
        i = float(request.form.get('i'))
        n = int(request.form.get('n'))

        # Convert annual interest rate to monthly and then to decimal
        monthly_rate = i / 12 / 100
        n_payments = n * 12

        M = calculate_sip(P, monthly_rate, n_payments)
        total_invested = P * n_payments
        estimated_returns = M - total_invested

    return render_template('sip_calculator.html', P=P, i=i, n=n, M=M, total_invested=total_invested, estimated_returns=estimated_returns)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

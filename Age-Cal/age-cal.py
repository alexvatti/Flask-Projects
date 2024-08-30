from flask import Flask, render_template, request
from datetime import datetime, date

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def age_calculator():
    age = None
    error = None
    
    if request.method == 'POST':
        dob_str = request.form.get('dob')
        today_str = request.form.get('today')
        
        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            today = datetime.strptime(today_str, '%Y-%m-%d').date()

            if today >= dob:
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            else:
                error = "Today's date cannot be before the date of birth."
        except ValueError:
            error = "Invalid date format."

    return render_template('age_calculator.html', age=age, error=error)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

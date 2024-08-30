from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

# Function to get BMI category
def get_bmi_category(bmi):
    if bmi < 16:
        return "Severe Thinness", "#FF0000"
    elif 16 <= bmi < 17:
        return "Moderate Thinness", "#FF4500"
    elif 17 <= bmi < 18.5:
        return "Mild Thinness", "#FF8C00"
    elif 18.5 <= bmi < 25:
        return "Normal", "#008000"
    elif 25 <= bmi < 30:
        return "Overweight", "#FFFF00"
    elif 30 <= bmi < 35:
        return "Obese Class I", "#FFA500"
    elif 35 <= bmi < 40:
        return "Obese Class II", "#FF6347"
    else:
        return "Obese Class III", "#FF0000"

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None
    color = None

    if request.method == 'POST':
        height = float(request.form.get('height', 0))
        weight = float(request.form.get('weight', 0))
        
        if height > 0:
            bmi = calculate_bmi(weight, height)
            category, color = get_bmi_category(bmi)
        else:
            error = "Height must be greater than zero."

    return render_template('bmi_calculator.html', bmi=bmi, category=category, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    weight = data.get('weight')
    height = data.get('height')
    
    if weight is None or height is None:
        return jsonify({"error": "Weight and height are required."}), 400
    
    try:
        bmi_value = calculate_bmi(weight, height)
        return jsonify({"bmi": bmi_value}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    weight = data.get('weight')
    height = data.get('height')
    age = data.get('age')
    gender = data.get('gender')
    
    if weight is None or height is None or age is None or gender is None:
        return jsonify({"error": "Weight, height, age, and gender are required."}), 400
    
    try:
        bmr_value = calculate_bmr(weight, height, age, gender)
        return jsonify({"bmr": bmr_value}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
        
@app.route('/')
def home():
    return "Bienvenue sur le service de calcul de santé ! Utilisez les endpoints /bmi et /bmr."

if __name__ == '__main__':
    app.run(debug=True)
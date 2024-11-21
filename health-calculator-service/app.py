from flask import Flask, request, jsonify, render_template_string
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "service": "Health Calculator Microservice",
        "available_endpoints": [
            {
                "path": "/bmi",
                "method": "POST",
                "description": "Calculate Body Mass Index",
                "required_params": ["height", "weight"]
            },
            {
                "path": "/bmr",
                "method": "POST", 
                "description": "Calculate Basal Metabolic Rate",
                "required_params": ["height", "weight", "age", "gender"]
            }
        ]
    })

# Vos routes existantes restent identiques...

@app.route('/bmi', methods=['POST'])
def bmi():
    try:
        data = request.json
        height = data['height']
        weight = data['weight']
        if height <= 0 or weight <= 0:
            return jsonify({"error": "Height and weight must be positive numbers"}), 400
        result = calculate_bmi(height, weight)
        return jsonify({"bmi": result})
    except KeyError as e:
        return jsonify({"error": f"Missing key: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bmr', methods=['POST'])
def bmr():
    try:
        data = request.json
        height = data['height']
        weight = data['weight']
        age = data['age']
        gender = data['gender']
        if height <= 0 or weight <= 0 or age <= 0:
            return jsonify({"error": "Height, weight, and age must be positive numbers"}), 400
        result = calculate_bmr(height, weight, age, gender)
        return jsonify({"bmr": result})
    except KeyError as e:
        return jsonify({"error": f"Missing key: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
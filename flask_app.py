from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the saved model
with open('Digital_prodact.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')

    # Make predictions using your model
    prediction = loaded_model.predict(pd.DataFrame({'JAHR': [year], 'MONAT': [month]}))

    # Assuming prediction is a numeric value
    prediction_value = prediction[0]

    response = {"prediction": prediction_value}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

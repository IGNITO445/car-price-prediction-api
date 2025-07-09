from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load('car_price_model.pkl')

# Define feature column order used in training
feature_columns = [
'Year', 'Mileage', 'EngineV', 'Brand_BMW',
    'Brand_Mercedes-Benz', 'Brand_Mitsubishi',
    'Brand_Renault', 'Brand_Toyota', 'Brand_Volkswagen',
    'Body_hatch', 'Body_other', 'Body_sedan', 'Body_vagon',
    'Body_van', 'Engine Type_Gas', 'Engine Type_Other',
    'Engine Type_Petrol', 'Registration_yes'
    # 👈 Your list may be longer or different
]


# Initialize Flask app
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convert incoming JSON to ordered feature vector
    input_data = [data.get(col, 0) for col in feature_columns]
    input_array = np.array(input_data).reshape(1, -1)

    # Predict the price
    predicted_price = model.predict(input_array)[0]

    return jsonify({'predicted_price': round(predicted_price, 2)})


if __name__ == '__main__':
    app.run(debug=True)

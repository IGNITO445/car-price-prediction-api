from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load model
with open("car_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load training columns used after one-hot encoding
with open("model_columns.pkl", "rb") as f:
    training_columns = pickle.load(f)


@app.route('/')
def home():
    return "Car Price Prediction API is running."


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input
        data = request.get_json(force=True)
        input_df = pd.DataFrame([data])

        # One-hot encode like during training
        input_df = pd.get_dummies(input_df)

        # Align with training columns
        input_df = input_df.reindex(columns=training_columns, fill_value=0)

        # Predict
        prediction = model.predict(input_df)[0]
        return jsonify({'predicted_price': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

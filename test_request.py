import requests

def test_prediction_api():
    url = 'http://127.0.0.1:5000/predict'
    data = {
        "Brand": "Toyota",
        "Body": "sedan",
        "Mileage": 50000,
        "EngineV": 2.0,
        "Engine Type": "Petrol",
        "Registration": "yes",
        "Year": 2018,
        "Model": "Corolla"
    }

    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response:", response.json())

test_prediction_api()



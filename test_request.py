import requests

url = 'http://127.0.0.1:5000/predict'

data = {
    'Year': 2015,
    'Mileage': 60000,
    'EngineV': 2.0,
    'Brand_BMW': 1,
    'Brand_Toyota': 0,
    'Body_SUV': 1,
    'Engine Type_Diesel': 1,
    'Registration_yes': 1
    # ➕ Add any missing features from your actual feature_columns list
}

response = requests.post(url, json=data)
print(response.json())
if __name__ == '__main__':
    response = requests.post(url, json=data)
    print(response.json())


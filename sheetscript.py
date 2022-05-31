import logging

import requests
SHEETY_ENDPOINT = 'https://api.sheety.co/cd5ffcb6d2166046577b57e44986fbf5/hrBot/prices'

data = {
    "price": {
        "a": "X",
        "b": "Y"
    }
}

response = requests.post(url=SHEETY_ENDPOINT, json=data)
logging. basicConfig()
print("response.status_code =", response.status_code)
print("response.text =", response.text)
import requests

def extract(url, params):
    try:
        response = requests.get(url, params = params)
        data = response.json()
        print(data)
    except Exception as e:
        pass


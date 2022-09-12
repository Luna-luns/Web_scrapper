import requests

url = input('Input the URL:\n')
response = requests.get(url)
try:
    print(response.json()['content'])
    if not response.status_code:
        raise KeyError
except Exception:
    print('Invalid quote resource!')

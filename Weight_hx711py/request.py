import requests, json
URL = '192.168.0.9' 
response = requests.get(URL) 
response.status_code 
response.text

data = {'outer': {'inner': 'value'}} 
res = requests.post(URL, data=json.dumps(data))
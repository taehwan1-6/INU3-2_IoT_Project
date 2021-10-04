import requests, json
URL = 'http://52.79.170.214:8080/useHistory' 



# data = {"serialNumber":"juhwan0815","startWeight":500}
data = {"useHistory":{"serialNumber": "juhwan0815", "useAmount": 30}}
res = requests.post(URL, data=json.dumps(data),headers={'Content-Type': 'application/json'})
print(res.status_code)
print(res.text)
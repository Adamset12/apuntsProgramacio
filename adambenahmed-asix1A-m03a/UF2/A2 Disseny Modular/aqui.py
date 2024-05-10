import requests

city = 'barcelona'
api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': '45c4LvN+DaTUBcs+s02+rA==kaxckvAfVvIony8z'})
if response.status_code == requests.codes.ok:
    print(response.text.split(",")[1])
else:
    print("Error:", response.status_code, response.text)
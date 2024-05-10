import requests

word = 'rhyme'
api_url = 'https://api.api-ninjas.com/v1/rhyme?word={}'.format(word)
response = requests.get(api_url, headers={'X-Api-Key': '45c4LvN+DaTUBcs+s02+rA==kaxckvAfVvIony8z'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
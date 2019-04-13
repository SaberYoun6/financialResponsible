import requests
import json
import urllib

customerId = 'Yuriprym'
apiKey= '75d1b1b6870f5014e38de3ff0ae6e3f5'


url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,	
}
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')
else: 
        print("An error has occured!")

def internet_on(Id,ap):
   try:
      urllib.urlopen('http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(Id,ap),timeout=1)
      return True
   except urllib.URLError as err:
       return False

   
url.internet_on()

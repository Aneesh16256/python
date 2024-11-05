import pprint
import json
import requests
response=requests.get("http://api.open-notify.org/iss-now.json")
print(response.text)
response=json.loads(response.text)
pprint.pprint(response)
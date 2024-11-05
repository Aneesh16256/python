import requests
import pprint
import json
from pprint import pprint
response=requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
print(response.text)
print(type(response.text))
response=json.loads(response.text)
pprint(response)
# for key,value in response.items():
#     print(f"{key}={value}")
# print(type(res))
# print("current latitude:",res.keys('iss_position'))





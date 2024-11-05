import requests
import pprint
import json
from pprint import pprint
d={'name':'aneesh',
   'age':22,}
response=requests.post("http://postman-echo.com/post",data=d)
# res=requests.post()
# print(d)
# print(response.status_code)
print(response.text)
# print(type(response.text))
# res=json.loads(response.text)
# pprint(res)
# print(type(res))
# print("current latitude:",res.keys('iss_position'))
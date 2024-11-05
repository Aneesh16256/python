import json
import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.nic.in/")
print(response.text)
soup_data=BeautifulSoup(response.text,'html.parser')
print(soup_data)
print(soup_data.find_all('h3'))
f1 = open("C:\\Users\\Aneesh.s\\OneDrive\\Desktop\\mypage.html","wb")
f1.write(response)
f1.close()
from urllib.request import urlopen
from bs4 import BeautifulSoup
data=urlopen("https://www.nic.in/").read()
print(data)
soup_data=BeautifulSoup(data,'html.parser')
print(soup_data)
print(soup_data.find_all('h3'))
f1 = open("C:\\Users\\Aneesh.s\\OneDrive\\Desktop\\mypage.html","wb")
f1.write(data)
f1.close()
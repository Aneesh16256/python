import re
data="my name is aneesh my gmail is aneeshaswany234@gmail.com"
pattern="[0-9a-z]+@[0-9a-z]+"
ans=re.findall(pattern,data)
print(ans)
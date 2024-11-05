import re
data="my name is aneesh my phone number is 9745754221"
pattern="[0-9]{10}"
ans=re.findall(pattern,data)
substitute=re.sub(pattern,"************",data)
print(substitute)
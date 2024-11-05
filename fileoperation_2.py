f=open(r"C:\Users\Aneesh.s\OneDrive\Desktop\v\India.txt","r")
content=f.read()
x=content.upper()
print(x)
f.close()
f1 = open("C:\\Users\\Aneesh.s\\OneDrive\\Desktop\\New\\INDIA.txt","w")
f1.write(x)
f1.close()


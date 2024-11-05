# f = open(r"C:\Users\Aneesh.s\OneDrive\Desktop\v\hi aneesh.txt","r")
# content = f.read()
# print(content)
# f.close()

# r - read
# w - write
# a - append
# t - textmode
# b - binary mode

f1 = open("foo.txt", "wt")
f1.write("This is techzmatrix python batch students\n")
f1.write("Anish - present\n")
f1.write("Sankari present\n")
f1.write("Sabari present\n")
f1.close()

f1 = open("foo.txt", "at")
f1.write("Hari present\n")
f1.close()

with open("foo.txt", "at") as f2:
    f2.write("Vishnu Present\n")

'''
1. create a file with "india.txt" content " india is my country"
Read the content of the file 
convert all words to capital letters
create a newfile names INDIA.txt and write the content to it
'''

'''name="Aneesh"
name=input("enter your name:")
age=int(input("enter your age:"))
print("hello",name,"you are",age,"years old")
print(type(age))
'''
#arithematical operator
'''
x=15
y=4
print("addition=",x+y)
print("subtraction=",x-y)
print("multiplication=",x*y)
print("division=",x/y)
print("modulus=",x%y)
print("Fdivision=",x//y)
print("exponent=",x**y)
'''
#comaprison operators
'''
x=15
y=4
print("equal",x==y)
print("notequal",x!=y)
print("greater than",x>y)
print("less than",x<y)
'''
#logical operators
'''
x=True
y=False
print("AND",x and y)
print("OR",x or y)
print("NOT", not x)
'''
#identity operator

'''x="hello"
print('e' in x)
print('1' in x)
print('o'not in x)
'''
'''x='hello'
y='hello'
print(x is y)
print(x is not y)'''

#DATA TYPES
#STRING (ORDERED AND IMMUTABLE COLLECTION)
'''x="techzmatrix"
print(x[0])
print(x)'''

#SLICING
'''
x="techzmatrix"
print(x[0:4])
print(x[1:4])
print(x[::-2])
print(x[::-3])
print(x[-4:-1])
print(x[-3:-1])
'''
#upper and lower case
'''
college="indian institute of technology"
print(college .upper())
print(college.lower())
'''

#strip(removes extra spaces)
'''
college="indian institute of technology"
print(college.strip())
'''
'''
college="indian institute of technology"
print(college.strip('i'))
'''
'''
college="indian institute of technology"
print(college.strip('t'))
'''
'''#REPLACE
college="indian institute of technology"
print(college.replace ("indian institute of technology","attingal engineering college"))
'''
'''
a=input("enter you mail id: ")
x=a.split('@')
y=x[1].split('.')
print(y[0])

'''
'''
l1=[2.5,3,"python",100]
print(l1[1])
l1[1]=20.25
print(l1)
'''
'''
l2=[5,10,20,[500,700,1000],'usa']
l2[3][2]='japan'
print(l2)
'''
#append(adds an element to the end of the list)
'''
l1=[1,2,3]
l1.append(4)
print(l1)
'''
#extend(add all the elements of another list to the initial list)
'''
l1=[1,2,3]
print(l1.extend((6,7,8)))
print(l1)
'''
#or
'''l1=[1,2,3]
l2=[10,20,30]
l1.extend(l2)
print(l1)'''

#insert 
#out put[1, 2, 100, 3]
#out put[1, 2, 100, 100, 3]
'''
l1=[1,2,3]
l1.insert(2,100)
print(l1)
l1.insert(3,100)
print(l1)
'''
'''
#remove
l1=[99,1,100,2,5]
l1.remove(100)
print(l1)
'''
#count
'''l1=[99,1,100,2,100,5]
print(l1.count(100))'''

#pop
'''
l1=[1, 2, 100, 100, 3]
print(l1.pop(2))''''''
print(l1)
print(l1.pop()) #paranthesis shows that print the last value in the list
print(l1) #resultent list after the pop up 
'''
#INDEX(TO KNOW THE POSITION OF PARTICULAR VALUE)
'''l1=[1, 2, 100, 25]
print(l1.index(3))'''
#sort (arrangement is classified into two ascending arrangement and descending arrangement)
#ascending arrangement
'''
l1=[1, 2, 100, 25]
print(l1.sort())
print(l1)
'''
#descending arrangement
'''
l1=[1, 2, 100, 25]
print(l1.sort(reverse=True))
print(l1)
'''
#reverse
'''
l4=[1,5,8,9,3,2]
print(l4.reverse())
print(l4)
'''
#clear
'''
l4=[1,5,8,9,3,2]
print(l4.clear())
print(l4)
'''
#Tuple()(immutable)
'''
t1=(1,2,'python',5,10.5)
print(t1)
print(type(t1))
'''
#data set
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(type(s1))
'''
#set union(A/B)
'''
s1={10,20,30,40}
s2={30,40,50,60}
s1.union(s2)
print(s1.union(s2))
'''
#set union in another method
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1|s2)
'''
#intersection(common element)(A&B)
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.intersection(s2))
'''
#another method for intersection 
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1&s2)
'''
#difference(A-B and B-A)
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.symmetric_difference(s2))
'''
#other difference(A-B and B-A)
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s2-s1)
'''
#symmetric_difference(A^B)
'''
s1={10,20,30,40}
s2={30,40,50,60}#Unique elements in s1 (not in s2): 10 and 20.
print(s1.symmetric_difference(s2))#Unique elements in s2 (not in s1): 50 and 60.
'''
#other Symmetric difference()
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1^s2)
'''

#difference_update
#The difference_update method removes all elements from s1 that are also present in s2.
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.difference_update(s2))
print(s1)
'''
#Add function(similar to Append from list)
'''
s1={10,20,30,40}
print(s1.add(100))
print(s1)
'''
#update(similar to extend function in set)
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.update(s2))
print(s1)
'''
#pop
'''
s1={10,20,30,40}
print(s1.pop())
'''
#disjoint
#method returns "true" if none of the items are present in both sets,otherwise it returns "false"
'''
Checking if s1 and s2 are Disjoint:

* s1.isdisjoint(s2) checks if s1 and s2 have any elements in common.
* s1 contains the elements {10, 20, 30, 40}.
* s2 contains the elements {30, 40, 50, 60}.
* Both sets share the elements 30 and 40.
* Since they have common elements, s1.isdisjoint(s2) returns False.
* Since they have no common elements, s1.isdisjoint(s2) returns true.
'''
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))
'''
#Subset
'''
* s1 is subset of s2 in this case its not true its false
* s2 is subset of s1 in this case its not true its false
'''
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.issubset(s2))
print(s2.issubset(s1))
'''
#superset
'''
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.issuperset(s2))
print(s2.issuperset(s1))
'''
#Dictionary
'''
d1={'name':"Aneesh",'age':23,'grade':80,'class':10,'place':"tvm"}
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())
print(d1.get('name'))
print(d1.get('salary',25000))
print(d1.popitem())
print(d1.pop('name'))
print(d1.pop('salary',25000))
'''
#if condition
'''
n=int(input("enter the number: "))
if n>10:
    print('yes')
else:
    print('no')
'''
#elif condition
'''
n=int(input("enter the number: "))
if n>0:
    print('positive')
elif n==0:
    print('null')
else:
    print('negative')
'''
#for loop
'''
for i in [1,2,3,4,5]:
    print('hello world')
'''
'''
fruits=['apple','banana','chery']
for i in fruits:
    if i=="chery":
        break
    print(i)
'''
'''
fruits=['apple','banana','chery']
for i in fruits:
    if i=="banana":
        continue
    print(i)
'''
'''
for i in range(1,6):
    print(i)
'''
'''
for i in range(2,30,3):
    print(i)
'''
'''
for i in range(1,6):
    print(i)
else:
    print("loop is stoped")
'''
'''
for i in range(1,6):
    if i<=3:
        print(i)
else:
    print("loop is stoped")
'''
'''
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
'''
'''
for x in [0,1,2]:
    pass
'''
'''
#leap year
year=int(input("Enter a year: "))
#Check if the year is a leap year
if(year%4==0 and year%100!=0):
    print(f"{year} is a leap year.")
else:
    print(f"{year}is not a leap year.")
'''
#number is even or odd
'''
number=int(input("Enter a number: "))
if number%2==0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
'''
#input the number for the multiplication tabel
'''
number=int(input("enter a number: "))
print(f"multiplication table for {number}:")
for i in range(1,11):
    print(f"{number}x{i}={number*i}")
'''
'''
number=int(input("enter a number: "))
print("multiplication table for: ", number)
for i in range(1,11):
    print(str(i) + " x " + str(number) + " = " + str(number * i))
'''
'''
number1=int(input("enter number: "))
number2=int(input("enter number: "))
sum=(number1 + number2)
print(str(number1)+ "+" +str(number2) + "=" + str(sum))
'''
'''
number1=int(input("enter number1: "))
number2=int(input("enter number2: "))
sum=(number1 + number2)
print(f"{number1}+{number2}={sum}")
'''
#built in string methods
#capitalize()
'''
s="hello"
print(s.capitalize())
'''
#count
'''
s="techzmatrix software technologies"
print(s.count('o'))
print(s.count('o',5))
print(s.count('t'))  
print(s.count())
'''
#

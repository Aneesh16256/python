#square pattern
'''
n=5
for i in range(n):
    for j in range (n):
        print("*",end=' ')
    print()
'''
#traingle
'''
n=5
for i in range(n):
    for j in range (i+1):
        print("*",end=' ')
    print()
'''
#decreasing traingle
'''
n=5
for i in range(n):
    for j in range (i,n):
        print("*",end=' ')
    print()
'''
# right sided triangle
'''
n=5
for i in range(n):
    for j in range (i,n):
        print("-",end=' ')
    for j in range (i+1):
        print("*",end=' ')
    print()
'''
#pyramid
'''
n=5
for i in range(n):
    for j in range (i,n):
        print(" ",end=' ')
    for j in range (i):
        print("*",end=' ')
    for j in range (i+1):
        print("*",end=' ')
    print()
'''
#pyramid
'''
n=5
for i in range(n):
    for j in range (i,n):
        print(" ",end=' ')
    for j in range (i+1):
        print("*",end=' ')
    for j in range (i):
        print("*",end=' ')
    print()
 '''
'''
def second_largest(numbers):
    first = second = float('-inf')
    
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None
'''
#odd or even
'''
num=int(input("enter a number: "))
num91=num%2
print(f"number is {'even' if num1==0 else 'odd'}")
'''
# find the largest number
'''
num1=(input("enter a number1: "))
num2=(input("enter a number2: "))
num3=(input("enter a number3: "))
if num1>num2 and num1>num3:
     print("num1 is grater")
elif num2>num1 and num2>num3:
     print("num2 is grater")
elif num3>num1 and num3>num2:
     print("num3 is grater")
'''
#reverse string
'''
def reverse_string(input_string):
    return input_string[::-1]
input_string = (input("enter a string: "))
reversed_string = reverse_string(input_string)
if reversed_string == input_string:
    print("this is a paliondromic word")
else:
    print("not a paliandromic word")
'''
number=[1,3,2,4,5,7]
def second_largest(numbers):
    first = second = float('-inf')
    
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None
print(second_largest(number))
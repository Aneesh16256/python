# def <function_name> (<args,..>):
#     '''
#     function comments
#     '''
#     ...
#     return 

#Lambda  /anonymous fucntions

#normal method
def mul(x):
    mul=x*2
    return mul
print(mul(5))

# lambda method

double = lambda x:x*2
print(double(5))

#usual method

def add1(x,y,z=10):
    add1=x+y+z
    return add1
print (add1(2,3,3)) # Z is alredy assigned to 10 so if there is no number in the z postion it will add with 10

#lambda method

x=lambda x,y,z=0:x+y+z
print(x(3,4))
x=lambda x:x**3
print(x(3))
print((lambda a,b,c:a+b+c)(4,5,6))
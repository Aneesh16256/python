i=0
n1=0
n2=0
while (i<1):
    def myfunction(n1,n2):
        a=int(input("what do you want (add then press 1,sub press 2,mul press 3,exit from the loop press 0): "))
        if a==1:
            n1=int(input("enter number n1: "))
            n2=int(input("enter number n2: "))
            add=n1+n2
            return add
        if a==2:
            n1=int(input("enter number n1: "))
            n2=int(input("enter number n2: "))
            sub=n1-n2
            return sub
        if a==3:
            n1=int(input("enter number n1: "))
            n2=int(input("enter number n2: "))
            mul=n1*n2
            return mul
    print(myfunction(n1,n2))



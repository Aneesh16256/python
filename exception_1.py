# try:
#     x=10
#     y=0
#     print(x/y)
# except NameError:
#     print("it is not defined")
# except ZeroDivisionError:
#     print("y cannot be zero")
except Exception as error:
    print("an exception occured detail=",error)
# else:
#     print("nothing went wrong till now")
finally:
    print("this is final piece of code")



# age=-10
# try:
#     if age<0:
#         raise Exception("sorry age cannot be less than zero")
# except Exception as error:
#     print("exception occur",error)

# height=(input("enter your height: "))
# try:
#     height_in_inch=int(height)*2.45
#     print(height_in_inch)
# except Exception as error:
#     print("an exception occured.detail=",error)
# finally:
#     print("this is final piece of code")



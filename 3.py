list1=[1,2,3,4,5,5]
def duplicate():
    if list1==list(set(list1)):
        return True
    else:
        return False
print(duplicate())
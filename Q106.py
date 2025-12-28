tup=()

n = int(input("Enter how many elements you want to add in a tuple: "))

for i in range(0,n):
    num = int(input("Enter element you want to add:"))
    temp =(num,)
    tup = tup + temp
    
    
lst=[]

n = int(input("Enter how many elements you want to add in a list: "))

for i in range(0,n):
    num = int(input("Enter element you want to add:"))
    lst.append(num)
    
def listToTuple(tup,lst):
    x = tuple(lst)
    tup = tup + x
    
    return tup

print(f"Added list to tuple: {listToTuple(tup,lst)}")
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
arr=[]

n = int(input("Enter how many sub-list you want to add: "))

for i in range(1,n+1):
    list1=[]
    l_n = int(input(f"Enter how many elements you want to add in list {i} "))
    for j in range(1,l_n+1):
        num = int(input(f"Enter ele no {j} of List {i} :"))
        list1.append(num)
    arr.append(list1)

match=[]

m = int(input("Enter how many elements you want in a list for match: "))

for k in range(1,m+1):
    num = int(input(f"Enter element no {k}: "))
    match.append(num)

def isPresent(arr,match):
    for lis in arr:
        if lis == match:
            return True
    
    return False

if isPresent(arr,match):
    print("SubList found")
else:
    print("Sublist not found")
        
    
    
    

    
    
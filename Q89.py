lst=[]

n = int(input("Enter how many elements you want to add in a list: "))

for i in range(0,n):
    x = int(input("Enter element you want to add:"))
    lst.append(x)
 
num = int(input("Enter number to get its smallest closest: "))

def smallestClosest(lst,num):
    lst.sort()
    
    if num == lst[0]:
        return num
        
    for i in range(1,n):
        if lst[i] == num:
            return lst[i-1]
            
    return -1
        
    
if smallestClosest(lst,num) == -1:
    print("Element not in the list")
else:
    print(smallestClosest(lst,num))

list1 = []

n = int(input("Enter no. of elements you want to store in the list"))

for i in range(0,n):
    num = int(input(f"Enter number {i+1}:"))
    list1.append(num)
    
def findFirstDuplicate(list1):
    unique=set()
    
    for num in list1:
        if num in unique:
            return num
        unique.add(num)    

print(findFirstDuplicate(list1))
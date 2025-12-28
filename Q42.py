arr = []
n = int(input("Enter no. of elements you want to add: "))


for i in range(1,n+1):
    num = int(input(f"Enter {i} no. to add "))
    arr.append(num)
    
unique=set()
result=[]

for num in arr:
    if num in unique and not num in result:
        result.append(num)
    else:
        unique.add(num)
    
    
print(f"Sum of repeated numbers are: {sum(result)}")
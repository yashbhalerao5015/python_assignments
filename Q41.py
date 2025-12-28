arr = []
n = int(input("Enter no. of elements you want to add: "))
result = []

for i in range(1,n+1):
    num = int(input(f"Enter {i} no. to add "))
    arr.append(num)
    even = lambda x: result.append(x) if x%2 == 0 else None
    even(num)
    
    
print(result)
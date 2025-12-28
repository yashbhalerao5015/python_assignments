arr=[]
n = int(input("Enter no. of elements you want to add: "))

def isDifferent(arr,n):
    unique = set()
    
    for i in range(1,n+1):
        num = int(input(f"Enter ele no {i} :"))
        arr.append(num)
    
    for num in arr:
        if num not in unique:
            unique.add(num)
    
    if len(unique) == n:
        return True
    else:
        return False

print(isDifferent(arr,n))
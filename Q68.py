n = int(input("Enter no. of elements you want to add: "))
numbers=[]
for i in range(1,n+1):
    num = int(input(f"Enter ele no {i}: "))
    numbers.append(num)

def isMonotonic(numbers):
    asc_mon = sorted(numbers)
    desc_mon = asc_mon[::-1]
    
    if numbers == asc_mon or numbers == desc_mon:
        return True
    
if isMonotonic(numbers):
    print("Monotonic Array")
else:
    print("Not a Monotonic Array")
        
    
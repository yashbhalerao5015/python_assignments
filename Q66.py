n = int(input("Enter no. of elements you want to add: "))
numbers=[]
for i in range(1,n+1):
    num = int(input(f"Enter ele no {i}: "))
    numbers.append(num)

def countPositive(numbers):
    count=0
    for num in numbers:
        if num>0:
            count+=1
            
    return count
    
print(countPositive(numbers))
num = int(input("Enter a number to gets its divisor: "))

def numberOfDivisor(num):
    count=0
    for i in range(1,int((num/2))+1):
        if num%i==0:
            count+=1
            
    return count+1
            
print(f"Number of divisor of {num} is {numberOfDivisor(num)}")
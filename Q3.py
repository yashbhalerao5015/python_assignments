num = int(input("Enter number to check if its prime or not"))

def isPrime(num):
    for i in range(2,int((num/2))+1):
        if num%i == 0:
            return False
    return True
    
print(isPrime(num))
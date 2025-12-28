num = int(input("Enter a number "))
facto=[]
def factors(num,facto):
    
    for i in range(2,num+1):
        if num%i == 0:
            facto.append(i)
    

    
def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
    
def maxPrimeNum(facto):
    maxPrime=0
    
    for num in facto:
        if isPrime(num):
            maxPrime = max(num,maxPrime)
     
    return maxPrime
    
factors(num,facto)
print("Max Prime No: ",maxPrimeNum(facto))
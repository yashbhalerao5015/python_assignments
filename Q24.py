binary = input("Enter binary number: ")

def toDecimal(binary):
    decimal=0
    n = len(binary)
    
    for i in range(n):
        decimal += int(binary[i]) * (2 ** (n-i-1)) 
    return decimal 
    
print(toDecimal(binary))
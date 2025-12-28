n = int(input("Enter a number to check if it can be represented as difference of two squares or not: "))

def isSquares(n):
    if n%4 == 2:
        return False
    return True
    
if isSquares(n):
    print("It can be represented")
else:
    print("It cannot be represented")
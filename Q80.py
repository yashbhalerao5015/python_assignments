n = int(input("Enter n to get its tetrahedral number: "))

def tetrahedral(n):
    return int((n*(n+1)*(n+2))/6)
    
print(tetrahedral(n))
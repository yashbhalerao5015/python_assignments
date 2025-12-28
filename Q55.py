a = int(input("Enter a: "))
r = int(input("Enter r: "))
n = int(input("Enter n: "))

def geometricSeries(a,r,n):
    return a *(r**(n-1))
    
print(f"Geometric Series is {geometricSeries(a,r,n)}")
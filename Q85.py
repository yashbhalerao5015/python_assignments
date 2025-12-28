import math

r = int(input("Enter radius to get volume of sphere: "))

def surfaceAreaOfSphere(r):
    return 4/3 * math.pi * r **3
    
print(f"Surface area of sphere is {surfaceAreaOfSphere(r)}")
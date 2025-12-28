import math

r = int(input("Enter radius to get volume of sphere: "))

def volumeOfSphere(r):
    return 4/3 * math.pi* r**3
    
print(f"Volume of sphere is {volumeOfSphere(r)}")
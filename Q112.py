d = int(input("Enter diameter of cylinder: "))
h = int(input("Enter height of cylinder: "))

def perimeterOfCylinder(d,h):
    return (2*d)+(2*h)
    
print(f"Perimeter of Cylinder = {perimeterOfCylinder(d,h)}")
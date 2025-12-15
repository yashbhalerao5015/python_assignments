base = int(input("Enter base of traingular to find its volume "))
height = int(input("Enter height of traingular to find its volume "))
length = int(input("Enter length of traingular to find its volume "))
def volumeTriangular(b,h,l):
    return (1/2)*b*h*l

print(volumeTriangular(base,height,length))
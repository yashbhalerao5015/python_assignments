n = int(input("Enter nth term for centered hexagonal number: "))

def centeredHexagonal(n):
    return 3*(n)*(n-1)+1
    
print(f"nth term for centered hexagonal number is {centeredHexagonal(n)}")
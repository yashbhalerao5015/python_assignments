a = int(input("Enter a: "))
b = int(input("Enter b: "))

def facto(num):
    mult=1
    
    for i in range(num,1,-1):
        mult*=i
        
    return mult

ans = str(facto(b)/facto(a))
print(ans)
print(f"Last Digit: {ans[-1]}")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

def powerFun(a,b):
    return a ** b
    
def powerFunLoop(a,b):
    ans = 1
    for i in range(1,b+1):
        ans= ans*a
        
    return ans
    
print(f"a to the power b = {powerFun(a,b)}")
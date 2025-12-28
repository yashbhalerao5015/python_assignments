n = int(input("Enter number to convert it into binary: "))

def toBinary(n):
    ans = str(bin(n))
    return ans[2:]
    
print(toBinary(n))
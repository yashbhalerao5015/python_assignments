num = int(input("Enter number to check if its an undulating numbers: "))

def isUndulating(num):
    n = str(num)
    if len(n) < 3:
        return False
    
    x=n[0]
    for i in range(0,len(n),2):
        if x != n[i]:
            return False
        
    y=n[1]
    for j in range(1,len(n),2):
        if y != n[j]:
            return False
            
    return True
        
if isUndulating(num):
    print("Its an undulating number")
else:
    print("Its not an undulating number")
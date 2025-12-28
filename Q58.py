num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

def isSameSign(num1,num2):
    if num1 > 0 and num2 < 0:
        print("Both have different sign")
        return True
    
    if num1 < 0 and num2 > 0:
        print("Both have different sign")
        return True
        
    return False
        
if not isSameSign(num1,num2):
    print("Both have same sign")
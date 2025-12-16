num1 = int(input("Enter number one"))
num2 = int(input("Enter number two"))

def isDiffer(num1,num2):
    x = num1^num2
    binary = str(bin(x))
    binary = binary[2:]
    
    count = 0
    
    for ch in binary:
        if ch == '1':
            count+=1
            
    if count == 1:
        print("Differ by 1 bit")
    else:
        print("Differ not by 1 bit")
    
        
isDiffer(num1,num2)
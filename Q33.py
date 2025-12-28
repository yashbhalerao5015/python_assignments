decimal = int(input("Enter a decimal number "))

def toBinary(decimal):
    binary = bin(decimal)
    print(binary[2::])
    
toBinary(decimal)
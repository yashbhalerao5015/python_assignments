import re 

s = input("Enter a string:")

def sequence(s):
    result = re.findall(r"\b[a-z]+[_]+[a-z]+\b",s)
    
    print(result)
    
sequence(s)
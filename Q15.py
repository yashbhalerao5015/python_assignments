import re 

s = input("Enter a string:")

def splitString(s):
    result = re.split(r"[a-z]",s)
    result = [res for res in result if res]
    print(result)
    
splitString(s)
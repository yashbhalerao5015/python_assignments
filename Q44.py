import re 
string = input("Enter a string: ")
match = input("Enter a match string: ")

def matchingWord(string,match):
    pattern = r"\b^"+match+r"\b"
    
    ans = re.findall(pattern, string)
    
    if ans:
        return True
    else:
        return False
    
print(matchingWord(string,match))
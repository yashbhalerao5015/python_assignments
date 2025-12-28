import re 
string = input("Enter a string: ")

ans = re.findall("_[a-z]+_",string)
print(ans)
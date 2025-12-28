import re 
string = input("Enter a string: ")

delimeter = r"[&,@\s]+"
ans = re.split(delimeter,string)

print(ans)
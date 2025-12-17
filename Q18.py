string1 = input("Enter string1: ")
string2 = input("Enter string2: ")

for ch in string2:
    string1 = string1.replace(ch,"")
        
print(string1)
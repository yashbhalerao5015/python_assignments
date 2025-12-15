import re
sentence = input("Enter a setence")

print(re.findall(r"\b\w{4}\b",sentence))
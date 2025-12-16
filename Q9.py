s = input("Enter a string ")

def rotateStr(s):
    n = len(s)
    for i in range(1,n+1):
        rotated = s[i:] + s[:i]
        if rotated == s:
            return i
            
print(rotateStr(s))
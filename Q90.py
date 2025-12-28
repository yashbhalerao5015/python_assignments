string = input("Enter a string: ")

def longestWordLength(string):
    res = string.split(" ")
    
    maxLen = 0
    
    
    for word in res:
        maxLen = max(maxLen,len(word))
        if len(word) == maxLen:
            ans = word
        
    return [maxLen,ans]
    
print(longestWordLength(string))
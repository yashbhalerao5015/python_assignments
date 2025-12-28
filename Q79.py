word = input("Enter word: ")

def isOddLength(word):
    if len(word)%2 != 0:
        return True
    return False
    
if isOddLength(word):
    print("Word length is Odd")
else:
    print("Word length is not Odd")
string = input("Enter a string: ")

def isFirstLastSame(string):
    
    if len(string) == 1:
        return True
    
    if len(string)>1:
        if string[0] == string[-1]:
            return True
        else:
            return False
            
if isFirstLastSame(string):
    print("Same")
else:
    print("Not same")
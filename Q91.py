string_list=[["Hello From Yash"],["Great Weather"],["How you doing "],["GoodBye"]]

string = input("Enter a sub string to check if its present in list: ")

def isPresent(string):
    for lis in string_list:
        if string in lis:
            return True
            
    return False
        
if isPresent(string):
    print("Sub list is present in the string list")
else:
    print("Sub list is not present in the string list")
    
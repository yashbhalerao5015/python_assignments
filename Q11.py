import re 
string = input("Enter a string: ")
ch = input("Enter a charcter to remove its first and last occurence from string: ")

def removeFirstLast(string,ch):
    list1 = list(string)
    
    for c in list1:
        if c == ch:
            list1.remove(c)
            break;
            
    for i in range(len(list1)-1,-1,-1):
        if list1[i] == ch:
            list1.pop(i)
            break;
    result = "".join(list1)
    print(result)
    
removeFirstLast(string,ch)
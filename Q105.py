boolean_list=[True,False,True,True,True,False,True]

def countTrueBool(lst):
    count=0
    for value in lst:
        if value == True:
            count+=1
    
    return count
    
print(f"True boolean in list are {countTrueBool(boolean_list)}")
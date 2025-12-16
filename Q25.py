arr=[1,2,3,4,5,3,4,5,7]

def productNonRepeated(arr):
    unique = dict()
    
    for num in arr:
        if num in unique:
            unique[num] = unique.get(num)+1
        else:
            unique[num] = 1
    
    list1=[]
    
    for key in unique:
        if unique.get(key) == 1:
            list1.append(key)
            
    mult=1
    for lis in list1:
        mult*=lis
        
    return mult
    
print(productNonRepeated(arr))
lst=[[2,4],[4,5,6],[8,9],[7]]

def minLen(lst):
    minLen = len(lst[0])
    
    for lis in lst:
        minLen = min(minLen,len(lis))
        
    return minLen
    
print(f"minimum length of sublist is {minLen(lst)}")
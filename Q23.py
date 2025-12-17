list1=[[8,6,7],[45,55],[12,-1],[100,-5]]

def isMax(list1):
    
    ans = max(sum(lis) for lis in list1)
    return ans
    
print(isMax(list1))
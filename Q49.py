
arr= [[12,3,4],[5,6,7,8]]
def getElement(arr,index=0):
    ans = []
    for i in range(len(arr)):
        if len(arr) > 1:
            ans.append(arr[i][index])
            
    return ans

print(getElement(arr))    
           
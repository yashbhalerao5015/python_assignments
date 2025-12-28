arr = [1,2,4,5,7,8,10]

def findMissing(arr):
    missing=[]
    for i in range(len(arr)-1):
        if arr[i]+1 != arr[i+1]:
            for j in range(arr[i]+1,arr[i+1]):
                missing.append(j)
    print(missing)
    
findMissing(arr)
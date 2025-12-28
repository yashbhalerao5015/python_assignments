# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
arr=[4,2,2,8,3,3,1]

def countingSort(arr):
    
    #1. Find Max Element
    arr_max = max(arr)
    
    
    #2. Intialize array with 0 of size max element
    count=[]
    
    for i in range(0,arr_max+1):
        count.append(0)
        
    
    
    #3. Store Frequency with their index
    for num in arr:
        count[num] = count[num]+1
        
    
    
    #4. Do prefix Sum 
    for i in range(1,len(count)):
        count[i] = count[i]+count[i-1]
        
    
    
    #5. From the og array get the element, go at the index of it in prefix array subtract -1 from it and in output array at that position store the og element
    output=[]
    
    for i in range(0,len(arr)):
        output.append(0)
    
    for num in arr:
        count[num] = count[num]-1
        output[count[num]] = num
        
    print(output)
    
countingSort(arr)


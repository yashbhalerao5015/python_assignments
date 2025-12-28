arr=[2,4,2,4,1,3,5,2,6,7,5]


def frequency(arr):
    freq=dict()
    
    for num in arr:
        if num in freq:
            freq[num]= freq[num]+1
        else:
            freq[num] = 1
            
    print(f"Frequency of list elements are {freq}")
    
frequency(arr)


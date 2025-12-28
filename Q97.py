lst=[[2,4],[4,5,6],[8,9],[7]]

def frequencyCount(lst):
    freq=dict()
    
    for i in range(1,len(lst)+1):
        freq[i]=len(lst[i-1])
        
    print(freq)
        
frequencyCount(lst)
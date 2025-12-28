tuples=[(1,2),(4,5),(7,8),(10,11)]

print(tuples)

def isLenSame(tuples):
    for i in range(0,len(tuples)-1):
        
        if len(tuples[i]) != len(tuples[i+1]):
            return False
            
    return True
    
if isLenSame(tuples):
    print("All Tuples have equal length")
else:
    print("All Tuples dont have equal length")
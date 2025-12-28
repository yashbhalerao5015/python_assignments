
list1=[(3,14),(1,6),(5,166),(17,8)]

def maxDiff(list1):
    max_ele = 0
    ans=()
    for tup in list1:
        if (tup[1]-tup[0]) > max_ele:
            max_ele = tup[1]-tup[0]
            ans = tup
    
    return ans
    
print(f"Maximum difference of tuple list is {maxDiff(list1)}")
    
    

    
    
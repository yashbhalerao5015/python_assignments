list1 = [(1,2),(3,4),(5,6)]
list2 = [(1,2),(7,8),(3,4)]

def isSimilar(list1,list2):
    result=[]
    for li in list1:
        if li in list2:
            result.append(li)
    
    print(result)
    
isSimilar(list1,list2)
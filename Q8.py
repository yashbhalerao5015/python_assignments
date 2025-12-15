list1 = [1,2,3,4,5]

def squareList(list1):
    result=[]
    for ele in list1:
        sq = lambda n: n*n
        result.append(sq(ele))
    print(result)
    
squareList(list1)
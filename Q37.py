arr=[5,4,1,"abc","aa",-1]

num_list = []
str_list = []

def sortMixList(arr):
    for ele in arr:
        if type(ele) == int:
            num_list.append(ele)
        else:
            str_list.append(ele)
    
    result = []        
    num_list.sort()
    result.append(num_list)
    str_list.sort()
    result.append(str_list)
    
    final_res = []
    
    for lis in result:
        for ele in lis:
            final_res.append(ele)
            
    print(final_res)
    
sortMixList(arr)

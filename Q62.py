n = int(input("Enter no. of elements you want to add in list: "))
list1=[]
for i in range(1,n+1):
    num = int(input(f"Enter element no {i}: "))
    list1.append(num)


def minElement(list1):
    min_ele = list1[0]
    for num in list1:
        if num < min_ele:
            min_ele = num
    
    return min_ele
    
print(f"Min element from the list is {minElement(list1)}")
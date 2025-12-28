arr=[]
n = int(input("Enter no of elements you want to add: "))

for i in range(1,n+1):
    num = int(input(f"Enter no {i} to add in list: "))
    arr.append(num)
    
k = int(input("Enter kth no to get corresponsding ele: "))
def findKthEle(arr,k):
    return arr[k-1]
    
if k>0 and k<=len(arr):
    print(f"Element at kth position is {findKthEle(arr,k)}")
else:
    print("K is invalid")
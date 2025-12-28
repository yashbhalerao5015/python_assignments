arr=[]
n = int(input("Enter no of elements you want to add: "))

for i in range(1,n+1):
    num = int(input(f"Enter no {i} to add in list: "))
    arr.append(num)
    

def multAndDivide(arr):
    mult=1
    for num in arr:
        mult*=num
    return mult/len(arr)
    
print(f"Ans = {multAndDivide(arr)}")
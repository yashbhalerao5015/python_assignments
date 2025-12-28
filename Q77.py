arr=[1,2,3,4,5,6,7,8,9,10]

def differenceEvenOdd(arr):
    even=[]
    odd=[]
    for num in arr:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    return sum(even)-sum(odd)
    
print(f"Difference between sum of even and odd digits is {differenceEvenOdd(arr)}")
arr = [4,8,10,2,4,3,6,7,1]

def divisionEvenOdd(arr):
    even = 0
    odd = 0
    
    for num in arr:
        if num%2 == 0:
            even = num
            break
    
    for num in arr:
        if num%2 != 0:
            odd = num
            break
    
    return even/odd
    
print(divisionEvenOdd(arr))
arr=[36,6,12,24,100] 

def gcd(num1,num2):
    while num2!=0:
        temp = num1
        num1 = num2 
        num2 = temp%num2 
    return num1
    
def gcdArray(arr): 
    ans = gcd(arr[0],arr[1])
    
    for i in range(2,len(arr)):
        ans = gcd(ans,arr[i]) 
    return ans 
    

print(gcdArray(arr))
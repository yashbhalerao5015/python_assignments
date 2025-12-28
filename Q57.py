n = int(input("Enter a number: "))

def largestDigit(n):
    arr = [digit for digit in str(n)]
    arr.sort(reverse=True)
    ans = "".join(arr)
    return int(ans)
    
print(largestDigit(n))
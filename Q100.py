n = int(input("Enter a number to get its next smallest palindrome: "))

def isPalindrome(num):
    num_str = str(num)
    rev = num_str[::-1]
    
    if num == int(rev):
        return True

def smallestPalindrome(n):
    isTrue = True
    
    i = n
    while isTrue:
        if isPalindrome(i+1):
            isTrue = False
            return i+1
        i+=1
 
print(smallestPalindrome(n))  
    
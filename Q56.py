n = int(input("Enter a number: "))

def lessThanTwice(n):
    rev = str(n)
    rev = rev[::-1]
    rev = 2*(int(rev))
    
    if rev == n+1:
        return True
    else:
        return False

if lessThanTwice(n):
    print("Number is one less than twice of reverse")
else:
    print("Number is not one less than twice of reverse")
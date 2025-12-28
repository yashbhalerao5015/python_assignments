n = int(input("Enter n: "))
k = int(input("Enter k: "))

if k > n:
    k = int(input("k cannot be greater than n Enter k: "))
    
def facto(num):
    mult=1
    for i in range(num,1,-1):
        mult*=i
    
    return mult
    
binomial = facto(n)/(facto(k)*facto(n-k))

print(binomial)
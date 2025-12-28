num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
n = int(input("Enter n:"))

deno = max(num1,num2)
numo = min(num1,num2)

res = str(numo/deno)
if n <len(res) and n>0:
    print(res[n-1])
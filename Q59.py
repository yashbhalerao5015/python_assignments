n = int(input("Enter a number: "))

def nOctagonalSeries(n):
    return n*((3*n)-2)
    
print(f"nth term of octagonal series is {nOctagonalSeries(n)}")
tuples=[(12,8),(20,16)]

k = int(input("Enter k to check if it divides: "))

def isDivisible(tuples,k):
    
    for tup in tuples:
        for ele in tup:
            if ele%k != 0:
                return False
                
    return True
    

if isDivisible(tuples,k):
    print(f"Tuples are divisible by {k}")
else:
    print(f"Tuples are not divisible by {k}")
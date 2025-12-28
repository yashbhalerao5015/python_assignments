n = int(input("Enter nth term for newmany conway sequence: "))

def newmanConway(n):
    p=[]
    p.append(0)
    p.append(1)
    p.append(1)
    
    for i in range(3,n+1):
        p.append(p[p[i-1]]+p[i-p[i-1]]);
        
    return p[n]

print(f"Nth term for newman conway sequence is {newmanConway(n)}")
           
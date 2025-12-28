arr= [(4,"yash"),(1,"rajesh"),(2,"bhalerao")]
def sortList(arr):
    return sorted(arr,key=lambda x: x[0])

print(sortList(arr))
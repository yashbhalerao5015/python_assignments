import heapq
list1 = [5,4,3,2,1]
n = int(input("Enter n"))
if n <= len(list1):
    heapq.heapify(list1)
    print(heapq.nsmallest(n,list1))
else:
    print("n is larger than list size")
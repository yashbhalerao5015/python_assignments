from collections import Counter 
arr = [[1,2,3,4,1,2,4],[5,6,7,7],[2,3],[8,9]]

for lis in arr:
    print(Counter(lis))
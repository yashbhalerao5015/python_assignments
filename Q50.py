
arr= [[12,3,4],[5,6,7,8],[5]]
def minLen(arr):
    return min(arr,key=lambda x: len(x))

print(minLen(arr)) 
arr = [1,2,3,2,5,6,5]

arr =sorted(arr)

for i in range(0,len(arr)-1):
    if arr[i]==arr[i+1]:
        print(f"Duplicate Element: {arr[i]}")
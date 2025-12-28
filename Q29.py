list1 = [1,2,3,4,1,2,2,3,7,8,1,2,3,9]

frequency = {}

for num in list1:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num] = 1

for num in frequency:
    if frequency[num]%2 != 0:
        print(num)
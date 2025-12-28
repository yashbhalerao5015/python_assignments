string = "yashb"
def findChar(string):
    total = 0
    for i in range(len(string)):
        total += ord(string[i]) - ord('a')

    total = total % 26
    return chr(total + ord('a'))

print(findChar(string))
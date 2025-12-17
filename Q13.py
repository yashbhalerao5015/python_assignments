words={
    "eraser":5,
    "pen":2,
    "books":3,
    "pencil":6
}

def mostCommon(words):
    maxValue = max(words.values())
    result = [key for key,value in words.items() if value == maxValue]
    print(result)
    
mostCommon(words)
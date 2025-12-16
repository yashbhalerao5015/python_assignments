import re 
sentence = "My1 Na2me 4 is Ya5sh Bha6lerao7"

def removeDigits(sentence):
    new_Sentence = re.sub("[0-9]","",sentence)
    print(new_Sentence)
    
removeDigits(sentence)
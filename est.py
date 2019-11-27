text = "Aasdefsgh!!!"

def dups(input):
    charsFound = []
    count = 0
    x = 0
    while(x < len(input)):
        if(input[x] not in charsFound):
            print(input[x])
            tempText = input[x]
            input = input[:x] +input[x+1:]
            print(input)
            if(isIn(tempText, input)):
                charsFound.append(tempText)
                count+=1
        x+=1
    return count

def isIn(char, text):
    for x in range(len(text)):
        if(text[x] == char):
            print("yes")
            return True
    return False

print(dups(text))

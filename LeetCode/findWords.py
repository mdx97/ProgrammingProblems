def findWords(words):
    topRow = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
    midRow = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
    botRow = ["Z", "X", "C", "V", "B", "N", "M"]
    
    def getRow(c):
        row = -1
        c = c.upper()

        if (c in topRow):
            row = 0
        elif (c in midRow):
            row = 1
        elif (c in botRow):
            row = 2
        
        return row
    
    validWords = []

    for word in words:
        validWord = True
        row = -1

        for c in word:
            charRow = getRow(c)
            if row == -1:
                row = charRow
            else:
                if (charRow != row):
                    validWord = False
        
        if (validWord):
            validWords.append(word)
    
    return validWords
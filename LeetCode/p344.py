def reverseString(s):
    charStack = []
    for c in s:
        charStack.append(c)
        
    reversed = ""
    while (len(charStack) > 0):
        reversed += charStack.pop()

    return reversed
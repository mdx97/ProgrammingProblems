class Solution:
    def reverseString(self, s):
        char_stack = []
        for c in s:
            char_stack.append(c)
        reversed = ""
        while (len(char_stack) > 0):
            reversed += char_stack.pop()

        return reversed
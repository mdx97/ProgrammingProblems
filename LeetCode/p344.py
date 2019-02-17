class Solution:
    def reverseString(self, s):
        char_stack = []
        for c in s:
            char_stack.append(c)
        reverse = ""
        while (len(char_stack) > 0):
            reverse += char_stack.pop()

        return reverse

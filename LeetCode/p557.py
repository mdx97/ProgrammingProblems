class Solution(object):
    def reverseWords(self, s):
        output = ''
        last_space = -1
        for i, c in enumerate(s):
            if c == ' ':
                for j in range(i - 1, last_space, -1):
                    output += s[j]
                output += ' '
                last_space = i
        
        for j in range(len(s) - 1, last_space, -1):
            output += s[j]
                
        return output
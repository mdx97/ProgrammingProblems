class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        patternRepresentation = self.stringToDigitRepresentation(pattern)
        matches = []
        for word in words:
            if (self.stringToDigitRepresentation(word) == patternRepresentation):
                matches.append(word)

        return matches
    
    def stringToDigitRepresentation(self, string):
        dictionary = {}
        nextInt = 1
        representation = ""
        for c in string:
            if (c not in dictionary):
                dictionary[c] = nextInt
                nextInt += 1
            representation += str(dictionary[c])

        return representation

sol = Solution()
print (sol.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
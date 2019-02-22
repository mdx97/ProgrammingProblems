class Solution(object):
    def toGoatLatin(self, S):
        words = S.split()
        new = [] 
        for idx, word in enumerate(words):
            new_word = self.convertWord(word)
            new_word += ("a" * (idx + 1))
            new.append(new_word)
        return " ".join(new)
    
    def convertWord(self, word):
        first_letter = word[0] 
        if not self.isVowel(first_letter):
            word = word[1:]
            word += first_letter
        return word + "ma"

    def isVowel(self, letter):
        return letter.lower() in set(['a', 'e', 'i', 'o', 'u'])

sol = Solution()
print(sol.toGoatLatin("I speak Goat Latin"))

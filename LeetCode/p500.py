class Solution:
    def findWords(self, words):
        top_row = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
        mid_row = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
        bot_row = ["Z", "X", "C", "V", "B", "N", "M"]
        
        def get_row(c):
            row = -1
            c = c.upper()
            if (c in top_row):
                row = 0
            elif (c in mid_row):
                row = 1
            elif (c in bot_row):
                row = 2
            return row
        
        valid_words = []

        for word in words:
            valid_word = True
            row = -1

            for c in word:
                char_row = get_row(c)
                if row == -1:
                    row = char_row
                else:
                    if (char_row != row):
                        valid_word = False
            
            if valid_word:
                valid_words.append(word)
        
        return valid_words
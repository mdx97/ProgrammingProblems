# This is not the optimal solution (in regard to complexity analysis).
# The optimal solution uses a Trie I think.
class Solution(object):
    def longestWord(self, words):
        words.sort()
        parts = set()
        longest = ""
        for word in words:
            if len(word) == 1 or word[:-1] in parts:
                parts.add(word)
                if len(word) > len(longest):
                    longest = word
        return longest

sol = Solution()
print(sol.longestWord(["w", "wo", "wor", "world", "world"]))
class Solution:
    def reverseVowels(self, s):
        vowels = set(["a", "e", "i", "o", "u"])
        lo = 0
        hi = len(s) - 1
        chars = list(s)

        while hi > lo:
            while lo < len(s) and chars[lo].lower() not in vowels:
                lo += 1
            while hi > 0 and chars[hi].lower() not in vowels:
                hi -= 1
            if not (hi > lo):
                break

            temp = chars[hi]
            chars[hi] = chars[lo]
            chars[lo] = temp
            lo += 1
            hi -= 1

        return "".join(chars)


sol = Solution()
print(sol.reverseVowels("leetcode"))

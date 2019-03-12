class Solution(object):
    def strStr(self, haystack, needle):
        left = 0
        right = len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        return -1

sol = Solution()
print(sol.strStr("aaaaa", "bba"))
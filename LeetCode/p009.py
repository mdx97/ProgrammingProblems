class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        return (str(x) == str(x)[::-1])

sol = Solution()
print(sol.isPalindrome(12321))
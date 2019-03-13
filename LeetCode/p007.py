# The solution is correct. Leetcode won't accept because of an overflow test case.
# Solution is O(d) where d is the number of digits in x.
# This solution must iterate through the digits in x twice to keep O(1) space complexity.
# You could trade that extra iteration for O(d) space complexity. (Using a stack or array).
class Solution(object):
    def reverse(self, x):
        is_negative = x < 0
        x = abs(x)
        digits = 0
        temp = x
        while temp > 0:
            temp //= 10
            digits += 1
        exp = digits - 1
        rev = 0
        while x > 0:
            digit = x % 10
            rev += digit * 10**exp
            exp -= 1
            x //= 10
        return rev if not is_negative else -rev

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
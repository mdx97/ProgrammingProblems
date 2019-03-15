class Solution(object):
    def twoSum(self, numbers, target):
        lo = 0
        hi = len(numbers) - 1
        while 1:
            temp_sum = numbers[lo] + numbers[hi]
            if temp_sum == target:
                return [lo, hi]
            elif temp_sum > target:
                hi -= 1
            else:
                lo += 1

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
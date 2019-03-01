class Solution(object):
    def twoSum(self, nums, target):
        dictionary = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in dictionary and dictionary[complement] != idx:
                return [dictionary[complement], idx]
            dictionary[num] = idx

    def twoSum_bf(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

sol = Solution()
print(sol.twoSum([3, 2, 4], 6))
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        idx = 1
        while idx < len(nums):
            if nums[idx] == nums[idx - 1]:
                del nums[idx]
                idx -= 1
            idx += 1
        
        return len(nums)

sol = Solution()
print(sol.removeDuplicates([1, 1, 1, 1, 2, 2, 2, 2, 4, 5, 8, 8, 8]))
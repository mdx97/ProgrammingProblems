class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# This solution has similar O(n) time complexity, but will exit execution the moment a duplicate is found.
# This will lead to better performance.
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for val in nums:
            if val in seen: return True
            seen.add(val)
        return False

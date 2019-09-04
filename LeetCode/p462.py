class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[len(nums) // 2]
        moves = 0
        
        for val in nums:
            moves += abs(m - val)
        
        return moves
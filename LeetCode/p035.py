# Naive Solution (Time Complexity: O(n))
class Solution1(object):
    def searchInsert(self, nums, target):
        for idx, num in enumerate(nums):
            if num >= target:
                return idx
        return len(nums)

# Binary Search Solution (Time Complexity: O(log(n))
class Solution2(object):
    def searchInsert(self, nums, target):
        def binary_search(left, right):
            mid = (left + right) // 2
            if left == right:
                return left
            elif nums[mid] == target or (nums[mid] > target and nums[mid - 1] < target):
                return mid
            elif nums[mid] > target:
                return binary_search(left, mid)
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
        return binary_search(0, len(nums))

sols = {"Naive": Solution1(), "Binary Search": Solution2()}
for key, sol in sols.items():
    print()
    print("Solution:", key)
    print(sol.searchInsert([1, 3, 5, 6], 5))
    print(sol.searchInsert([1, 3, 5, 6], 2))
    print(sol.searchInsert([1, 3, 5, 6], 7))
    print(sol.searchInsert([1, 3, 5, 6], 0))
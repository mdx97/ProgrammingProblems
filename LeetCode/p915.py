# Solution: Brute Force - Iterate through the array and check if all values up to and including i are less than all values after i.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution1(object):
    def partitionDisjoint(self, A):
        n = len(A) 
        for i in range(n):
            lower_max = max(A[:i + 1])
            upper_min = min(A[i + 1:])
            if lower_max <= upper_min:
                return i + 1
    
# Solution: Start at the maximum value in the list. Move pointer left if the value on the left is the next highest number. Requires having a sorted version of the array stored.
# Time Complexity: O(n log n)?
# Space Complexity: O(n)
class Solution2(object):
    def partitionDisjoint(self, A):
        sort = list(A)
        sort.sort()
        idx = self.getMaxIndex(A)
        sort_idx = -1
        while idx >= 0 and A[idx] == sort[sort_idx]:
            idx -= 1
            sort_idx -= 1
        return idx + 1

    def getMaxIndex(self, A):
        idx = 0
        for i in range(1, len(A)):
            if A[i] > A[idx]:
                idx = i
        return idx

class Solution(object):
    def partitionDisjoint(self, A):
        n = len(A)
        maxs = [0] * n
        mins = [0] * n
        maxs[0] = A[0]
        mins[-1] = A[-1]

        for i in range(1, n):
            maxs[i] = max(maxs[i - 1], A[i])

        for i in range(1, n):
            index = -(i + 1)
            mins[index] = min(mins[index + 1], A[index])

        for i in range(1, n):
            if maxs[i - 1] <= mins[i]:
                return i

sol = Solution()
arr = [5, 0, 3, 8, 6]
print(sol.partitionDisjoint(arr))

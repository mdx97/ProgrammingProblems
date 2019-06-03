# Solution: Basic Pascal's Triangle construction and returns the last row.
# Time Complexity: O(k^2)
# Space Complexity: O(k^2)
class Solution(object):
    def getRow(self, rowIndex):
        triangle = [[1 for x in range(rowIndex + 1)] for y in range(rowIndex + 1)]
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
        
        return triangle[rowIndex]

# Solution: Same idea as the first solution, except we only track the previous row.
# Time Complexity: O(k^2)
# Space Complexity: O(k)
class Solution2(object):
    def getRow(self, rowIndex):
        row = [1]
        for i in range(1, rowIndex + 1):
            newRow = [1 for x in range(i + 1)]
            for j in range(1, i):
                newRow[j] = row[j] + row[j - 1]
            row = newRow
        
        return row

sol = Solution2()
print(sol.getRow(5))
class Solution(object):
    def flipAndInvertImage(self, A):
        for i in range(0, len(A)):
            reversedArray = []
            for j in range(len(A[i]) - 1, -1, -1):
                reversedArray.append(A[i][j])
            A[i] = reversedArray
        
        for i in range(0, len(A)):
            for j in range(0, len(A[i])):
                if (A[i][j] == 1):
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        
        return A

sol = Solution()
print(sol.flipAndInvertImage([[1, 1, 0], [0, 1, 1], [1, 0, 1]]))
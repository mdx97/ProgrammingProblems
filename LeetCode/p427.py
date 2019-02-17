class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        return self.construct_quadtree(grid, 0, 0, len(grid))
    
    def construct_quadtree(self, grid, row, col, N):
        leaf = True
        if len(grid) > 1:
            val = grid[row][col]
            for i in range(N):
                for j in range(N):
                    if grid[row + i][col + j] != val:
                        leaf = False
                        break
                        
        if leaf:
            val = grid[row][col]
            is_val = True if val == 1 else False
            return Node(is_val, True, None, None, None, None)

        half_size = N // 2
        child_tl = self.construct_quadtree(grid, row, col, half_size)
        child_tr = self.construct_quadtree(grid, row, col + half_size, half_size)
        child_bl = self.construct_quadtree(grid, row + half_size, col, half_size)
        child_br = self.construct_quadtree(grid, row + half_size, col + half_size, half_size)
        val = child_tl.val or child_tr.val or child_bl.val or child_br.val
        return Node(val, False, child_tl, child_tr, child_bl, child_br)

sol = Solution()
grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
sol.construct(grid)
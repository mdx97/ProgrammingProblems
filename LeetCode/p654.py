from common import TreeNode

class Solution:
    def constructMaximumBinaryTree(self, nums):
        index = nums.index(max(nums))
        f_half = nums[:index]
        s_half = nums[index + 1:]
        node = TreeNode(nums[index])
        if (len(f_half) > 0):
            node.left = self.constructMaximumBinaryTree(f_half)
        if (len(s_half) > 0):
            node.right = self.constructMaximumBinaryTree(s_half)

        return node

sol = Solution()
sol.constructMaximumBinaryTree([3,2,1,6,0,5])

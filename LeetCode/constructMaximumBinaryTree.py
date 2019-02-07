class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums):
    index = nums.index(max(nums))
    fHalf = nums[:index]
    sHalf = nums[index + 1:]

    node = TreeNode(nums[index])

    if (len(fHalf) > 0):
        node.left = constructMaximumBinaryTree(fHalf)

    if (len(sHalf) > 0):
        node.right = constructMaximumBinaryTree(sHalf)

    return node

constructMaximumBinaryTree([3,2,1,6,0,5])
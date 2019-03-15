from common import Node

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        nodes = [root]
        traversal = []
        while nodes:
            level = [node.val for node in nodes]
            traversal.append(level)
            new = []
            for node in nodes:
                new.extend(node.children)
            nodes = new
        return traversal

children = [Node(1, []), Node(2, []), Node(3, [])]
root = Node(0, children)
sol = Solution()
print(sol.levelOrder(root))
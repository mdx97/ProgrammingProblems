class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        nodes = self.inorderTraversal(root.left)
        nodes.append(root.val)
        nodes.extend(self.inorderTraversal(root.right))
        return nodes
    
    def inorderTraversal_it(self, root):
        stack = []
        res = []
        curr = root
        while (curr or len(stack) > 0):
            while (curr):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.add(curr.val)
            curr = curr.right
        return res
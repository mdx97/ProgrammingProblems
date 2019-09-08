from common import TreeNode

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        forest = []
        to_delete_set = set(to_delete)
        
        if root.val not in to_delete_set:
            forest.append(root)
            
        def dfs(node, parent_deleted=False):
            deleted = node.val in to_delete_set
            
            if not deleted and parent_deleted:
                forest.append(node)
                
            for i, child in enumerate([node.left, node.right]):
                if child:
                    if dfs(child, deleted):
                        if i == 0:
                            node.left = None
                        else:
                            node.right = None
            
            return deleted
        
        dfs(root)
        return forest
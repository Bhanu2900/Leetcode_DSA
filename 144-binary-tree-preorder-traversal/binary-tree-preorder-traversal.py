# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val)   # Step 1: Visit root
            dfs(node.left)            # Step 2: Traverse left
            dfs(node.right)           # Step 3: Traverse right
        
        dfs(root)
        return result

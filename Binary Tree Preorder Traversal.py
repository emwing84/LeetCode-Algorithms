#by Jeff Young
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            return traverse_preorder(root)
    
def traverse_preorder(root):
    if root is None: 
        return []
    return([root.val] + 
           traverse_preorder(root.left) + 
           traverse_preorder(root.right))
        
#by Jeff Young
#Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return traverse_in_order(root)
    
def traverse_in_order(root):
    if root is None: 
        return []
    return(traverse_in_order(root.left) + 
        [root.val] + 
        traverse_in_order(root.right))
        
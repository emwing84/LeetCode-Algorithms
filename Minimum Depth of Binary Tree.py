#by Jeff Young
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return min_tree_height(root)
    
def min_tree_height(root):
    if root is None:
        return 0
    if root.left== None or root.right == None:
        return min_tree_height(root.left) + min_tree_height(root.right) + 1
    return 1 + min(min_tree_height(root.right), min_tree_height(root.left))
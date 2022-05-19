#by Jeff Young
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_tree_height(root)
    
def max_tree_height(root):
    if root is None:
        return 0
    return 1 + max(max_tree_height(root.right), max_tree_height(root.left))
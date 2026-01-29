# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        mx = []

        def trav(root, zag=True, ct=0):
            if not root:
                return
            mx.append(ct)
            if zag:
                trav(root.left, False, ct+1)
                trav(root.right, True, 1)
            else:
                trav(root.right, True, ct+1)
                trav(root.left, False, 1)

        trav(root, True, 0)
        trav(root, False, 0)

        return max(mx)
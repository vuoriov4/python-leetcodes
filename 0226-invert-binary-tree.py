# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root == None):
            return root
        else:
            self.invertChildren(root)
            return root
    
    def invertChildren(self, node):
        tmp = node.right
        node.right = node.left
        node.left = tmp
        if (node.left != None):
            self.invertChildren(node.left)
        if (node.right != None):
            self.invertChildren(node.right)
        

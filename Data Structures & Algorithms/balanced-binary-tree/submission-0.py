
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def checkHeight(node):
            if not node:
                return 0
            leftHeight = checkHeight(node.left)
            rightHeight = checkHeight(node.right)
            if abs(leftHeight - rightHeight) > 1:
                self.balanced = False
            return max(leftHeight, rightHeight) + 1
        checkHeight(root)
        return self.balanced
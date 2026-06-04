
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return []
        output.extend(self.inorderTraversal(root.left))
        output.append(root.val)
        output.extend(self.inorderTraversal(root.right))
        return output
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l1 = []

        def traversal(root, l1):
            if root is not None:
                traversal(root.left, l1)
                traversal(root.right, l1)
                l1.append(root.val)

        traversal(root, l1)
        return l1

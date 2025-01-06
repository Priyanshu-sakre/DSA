class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l1 = []

        def traversal(root, l1):
            if root is not None:
                l1.append(root.val)
                traversal(root.left, l1)
                traversal(root.right, l1)

        traversal(root, l1)
        return l1

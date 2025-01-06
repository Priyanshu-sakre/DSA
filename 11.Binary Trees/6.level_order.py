class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])  # Queue to store nodes for BFS

        while queue:
            level = []
            for _ in range(len(queue)):  # Process all nodes in the current level
                node = queue.popleft()
                level.append(node.val)

                # Add left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)  # Append the current level to the result

        return result

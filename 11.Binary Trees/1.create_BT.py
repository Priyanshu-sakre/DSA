class Solution:
    def createTree(self, root, l):
        if not l:
            return

        # Queue for level-order traversal
        queue = [root]
        i = 1  # Start from the second element in the list

        # Traverse the list and construct the tree
        while queue and i < len(l):
            current = queue.pop(0)

            # Assign left child
            if i < len(l) and l[i] is not None:
                current.left = Node(l[i])
                queue.append(current.left)
            i += 1

            # Assign right child
            if i < len(l) and l[i] is not None:
                current.right = Node(l[i])
                queue.append(current.right)
            i += 1

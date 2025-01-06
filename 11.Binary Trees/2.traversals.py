from sys import *
from collections import *
from math import *


# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getTreeTraversal(root):
    # Lists to store the traversals
    inorder, preorder, postorder = [], [], []

    # Helper function for In-Order Traversal
    def inorder_traversal(node):
        if not node:
            return
        inorder_traversal(node.left)
        inorder.append(node.data)
        inorder_traversal(node.right)

    # Helper function for Pre-Order Traversal
    def preorder_traversal(node):
        if not node:
            return
        preorder.append(node.data)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

    # Helper function for Post-Order Traversal
    def postorder_traversal(node):
        if not node:
            return
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        postorder.append(node.data)

    # Perform all traversals
    inorder_traversal(root)
    preorder_traversal(root)
    postorder_traversal(root)

    # Return the results as a list of lists
    return [inorder, preorder, postorder]

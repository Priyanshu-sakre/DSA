class Solution:
    # Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        while root.left:
            root = root.left
        return root.data

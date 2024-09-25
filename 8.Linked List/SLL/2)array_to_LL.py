class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def constructLL(self, arr):
        self.head = Node(arr[0])
        mover = self.head
        for i in range(1, len(arr)):
            temp = Node(arr[i])
            mover.next = temp
            mover = mover.next
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next


ll = Solution()
arr = [2, 3, 4, 5]
ll.constructLL(arr)

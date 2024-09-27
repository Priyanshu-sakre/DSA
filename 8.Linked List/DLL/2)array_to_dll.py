class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def constructDLL(self, arr):
        head = Node(arr[0])
        mover = head
        for i in range(1, len(arr)):
            temp = Node(arr[i])
            tail = temp
            mover.next = temp
            temp.prev = mover
            mover = mover.next
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        print(tail.data)


s = Solution()
s.constructDLL([1, 2, 3, 4, 5, 6])

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        new = Node(x)

        if not head:
            head = new
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

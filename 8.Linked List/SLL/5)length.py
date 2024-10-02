class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
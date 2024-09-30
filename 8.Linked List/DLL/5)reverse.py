class Solution:
    def reverseDLL(self, head):
        # return head of reverse doubly linked list
        if head is None or head.next is None:
            return head
        current = head
        last = None
        while current:
            last = current.prev
            current.prev = current.next
            current.next = last
            current = current.prev
        head = last.prev
        return head

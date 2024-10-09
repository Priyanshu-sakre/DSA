class Solution:
    # Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        current = head
        while current:
            if current.data == x:
                if not current.prev:
                    head = head.next
                    head.prev = None
                elif not current.next:
                    current.prev.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
            current = current.next
        return head

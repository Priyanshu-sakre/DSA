class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        if not head or not head.next:
            return head
        current = head.next
        while current:
            if current.prev.data == current.data:
                if not current.next:
                    current.prev.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
            current = current.next
        return head

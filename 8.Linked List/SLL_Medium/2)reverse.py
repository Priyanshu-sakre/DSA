class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
        head = prev
        return head

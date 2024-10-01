# ITERATIVE
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


# RECURSIVE
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head

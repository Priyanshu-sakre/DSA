class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        k = k % self.len1(head)
        for i in range(k):
            prev, current = self.last_element(head)
            current.next = head
            head = current
            prev.next = None
        return head

    def last_element(self, val1):
        prev = None
        current = val1
        while current.next:
            prev = current
            current = current.next
        return prev, current

    def len1(self, head):
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

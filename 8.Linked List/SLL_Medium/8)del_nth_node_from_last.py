# BRUTE
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if self.len1(head) - n + 1 == 1:
            head = head.next
            return head
        elif self.len1(head) - n + 1 >= self.len1(head):
            prev = None
            current = head
            while current.next:
                prev = current
                current = current.next
            prev.next = None
            return head
        else:
            count = 1
            temp = None
            current = head
            while current and count < self.len1(head) - n + 1:
                temp = current
                current = current.next
                count += 1
            temp.next = current.next
            return head


    def len1(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
# OPTIMAL
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fastp = head
        slowp = head

        # Move the fastp pointer N nodes ahead
        for i in range(n):
            fastp = fastp.next

        # If fastp becomes None, the Nth node from the end is the head
        if fastp is None:
            return head.next

        # Move both pointers until fastp reaches the end
        while fastp.next is not None:
            fastp = fastp.next
            slowp = slowp.next

        # Delete the Nth node from the end
        delNode = slowp.next
        slowp.next = slowp.next.next
        delNode = None
        return head

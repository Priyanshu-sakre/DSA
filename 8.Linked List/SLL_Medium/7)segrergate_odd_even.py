# BRUTE
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        total = []
        current = head
        while current:
            total.append(current.val)
            if not current.next:
                break
            current = current.next.next
        c2 = head.next
        while c2:
            total.append(c2.val)
            if not c2.next:
                break
            c2 = c2.next.next
        current = head
        count = 0
        while current:
            current.val = total[count]
            count += 1
            current = current.next
        return head
# OPTIMAL
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

# BRUTE
# either by list or by stack
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1 = []
        current = head
        while current:
            l1.append(current.val)
            current = current.next
        if l1 == l1[::-1]:
            return True
        return False
# OPTIMAL
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_head = self.reverse(slow.next)
        first = head
        second = new_head
        while second:
            if first.val != second.val:
                self.reverse(new_head)
                return False
            first = first.next
            second = second.next
        self.reverse(new_head)
        return True

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverse(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head

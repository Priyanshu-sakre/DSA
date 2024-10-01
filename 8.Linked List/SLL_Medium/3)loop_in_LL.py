# BRUTE
def detectCycle(head):
    # Write your code here.
    l1 = []
    current = head
    while current:
        if current in l1:
            return True
        l1.append(current)
        current = current.next
    return False


# BETTER
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_map = {}
        current = head
        while current:
            if current in hash_map:
                return True
            hash_map[current] = 1
            current = current.next
        return False
# OPTIMAL
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

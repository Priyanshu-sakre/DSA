# BRUTE
def lengthOfLoop(head: Node) -> int:
    # Write your code here
    l1 = []
    current = head
    while current:
        if current in l1:
            return len(l1) - l1.index(current)
        l1.append(current)
        current = current.next
    return 0
# BETTER
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        if not head:
            return 0
        l1 = {}
        current = head
        count = 0
        while current:
            if current in l1:
                return len(l1) - l1[current]
            l1[current] = count
            current = current.next
            count += 1
        return 0
# OPTIMAL
def lengthOfLoop(head: Node) -> int:
    # Write your code here
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return find_length(slow, fast)
    return 0


def find_length(slow, fast):
    count = 1
    fast = fast.next
    while slow != fast:
        count += 1
        fast = fast.next
    return count

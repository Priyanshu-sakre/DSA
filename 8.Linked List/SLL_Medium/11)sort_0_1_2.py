class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # code here
        l1 = []
        current = head
        while current:
            l1.append(current.data)
            current = current.next
        l1.sort()
        current = head
        count = 0
        while current:
            current.data = l1[count]
            count += 1
            current = current.next
        return head

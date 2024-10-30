# BRUTE
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
# BETTER
class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # code here
        count_0 = 0
        count_1 = 0
        count_2 = 0
        current = head
        while current:
            if current.data == 0:
                count_0 += 1
            elif current.data == 1:
                count_1 += 1
            else:
                count_2 += 1
            current = current.next
        current = head
        while current:
            if count_0:
                current.data = 0
                count_0 -= 1
            elif count_1:
                current.data = 1
                count_1 -= 1
            else:
                current.data = 2
                count_2 -= 1
            current = current.next
        return head
#OPTIMAL

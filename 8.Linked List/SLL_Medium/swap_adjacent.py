class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SLL:
    def __init__(self) -> None:
        self.head = None


n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
n4 = Node(400)
n5 = Node(500)
n6 = Node(600)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
sll = SLL()
sll.head = n1
current = sll.head
while current.next:
    current.val, current.next.val = current.next.val, current.val
    current = current.next.next
    if current == None:
        break
current = sll.head
while current:
    print(current.val, end=" ")
    current = current.next

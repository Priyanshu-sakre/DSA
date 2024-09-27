class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def traverse(self):
        if not self.head:
            print("Doubly LL is empty")
        else:
            current = self.head
            while current:
                print(current.val, end=" ")
                current = current.next
            print()


dll = DLL()
dll.insert_at_head(100)
dll.traverse()
dll.insert_at_head(50)
dll.traverse()
dll.insert_at_tail(200)
dll.traverse()

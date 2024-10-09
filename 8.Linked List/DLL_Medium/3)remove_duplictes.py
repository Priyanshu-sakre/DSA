def removeDuplicates(head: Node) -> Node:
    # Write your code here
    current = head.next
    while current:
        if current.data == current.prev.data:
            if current.next:
                current.prev.next = current.next
                current.next.prev = current.prev
            else:
                current.prev.next = None
        current = current.next
    return head

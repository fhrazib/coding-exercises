from linked_list import LinkedList, print_from_node


def reverse(head):
    current = head
    previous = None

    while current:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
    return previous


ll = LinkedList()
ll.append(2)
ll.append(4)
ll.append(6)

ll.append(16)
ll.append(60)
ll.append(611)
ll.append(613)
ll.append(6193)
ll.append(61111)
ll.append(613111)

ll.append(8)
ll.append(10)
ll.print()

reversed_head = reverse(ll.head)
print_from_node(reversed_head)

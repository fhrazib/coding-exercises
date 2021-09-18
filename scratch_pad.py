class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # contains the reference of the first node
        self.tail = None  # contains the reference of the last non-null node

    def append(self, data):  # without using tail
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def append_v2(self, data):  # with using tail
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.tail:
            self.tail.next = new_node
            self.tail = new_node

    def print_ll(self):
        current = self.head
        while current:
            print(hex(id(current)), ': ', current.data)
            current = current.next


ll = LinkedList()
ll.append(2)
ll.append(5)
ll.append(3)
ll.append(7)
ll.append(10)
ll.append(11)
ll.append(100)
ll.append(109)
ll.append(19)
ll.append(160)
ll.append(15)
ll.append(15)
ll.print_ll()

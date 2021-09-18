class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        pass

    def append_v2(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.tail:
            self.tail.next = new_node
            self.tail = new_node

    def print(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


ll = LinkedList()
ll.append_v2(1)
ll.append_v2(2)
ll.append_v2(3)
ll.append_v2(4)
ll.append_v2(5)
ll.append_v2(6)
ll.print()


ll2 = LinkedList()
ll2.append(5)
ll2.append(6)
ll2.append(7)
ll2.append(2)
ll2.append(44)
ll2.append(992)
ll2.append(2334)
ll2.print()
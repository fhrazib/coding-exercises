"""
# 1
    - here we are searching for a special node (the last node) - after that we can append our new node.
    - the one important property of the last node is that its has 'none' at it's next.
        - this property is unique to the last node; no other node has this property
    - so we set the loop condition here like 'current.next is not None'.
    - when we reach 'current.next=None' we exit the loop cause we got our last node

# 3
    - our intention is to print data here
    - so we only concern about valid node (all nodes which has a data part; all non 'None' nodes)
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # contains the reference of the first node
        self.tail = None  # contains the reference of the last non-null node

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:  # 1
                current = current.next
            current.next = new_node  # 2
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

    def print(self, print_address=False):
        current = self.head
        while current:  # 3
            if print_address:
                print(hex(id(current)).upper(), ': ', current.data)
            else:
                print(current.data, end=' ')
            current = current.next
        print()


def print_from_node(node):
    current = node
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


def main():
    print('Linked list append version 1: using while loop to iterate up to the last node')
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
    ll.print(True)

    print('\nLinked list append version 2: using tail; no iteration needed while appending new nodes')
    ll2 = LinkedList()
    ll2.append_v2(1)
    ll2.append_v2(2)
    ll2.append_v2(3)
    ll2.append_v2(5)
    ll2.append_v2(6)
    ll2.append_v2(9)
    ll2.append_v2(5)
    ll2.append_v2(9)
    ll2.append_v2(9)
    ll2.print()


if __name__ == "__main__":
    main()

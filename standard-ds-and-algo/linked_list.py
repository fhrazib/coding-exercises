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
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head:
            current = self.head
            while current.next:  # 1
                current = current.next
            current.next = new_node  # 2
        else:
            self.head = new_node

    def print_ll(self):
        current = self.head
        while current:  # 3
            print(current.data)
            current = current.next


ll = LinkedList()
ll.append(3)
ll.append(6)
ll.append(7)
ll.append(5)
ll.append(10)
ll.print_ll()

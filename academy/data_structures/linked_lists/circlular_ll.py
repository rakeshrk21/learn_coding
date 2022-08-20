class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f'Node {self.data}'

class CLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, data):
        self.size += 1
        return Node(data)

    def __iter__(self):
        node = self.head
        index = 0
        while index < self.size:
            yield node
            index += 1
            node = node.next

    def get_size(self):
        return self.size


if __name__ == "__main__":
    clist = CLinkedList()
    node0 = clist.add_node(0)
    node1 = clist.add_node(1)
    node2 = clist.add_node(2)
    node3 = clist.add_node(3)
    node4 = clist.add_node(4)
    clist.head = node0
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node0
    clist.tail = node4
    print(clist.size)
    print([item.data for item in clist])


class DNode:

    def __init__(self, data):
        if data is None:
            raise AttributeError("Data for node can't be None")
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'DNode {self.data}'


class DoublyLinkedList:

    def __init__(self, node):
        self.head = node
        self.tail = node
        self.size = 1
        node.prev = None

    def addNode(self, newNode):
        # iterate to the last node
        print(self.size)
        lastNode = self.getNodeAtIndex(self.size)

        # add the element tp the end of the ll
        newNode.prev = lastNode
        lastNode.next = newNode
        self.tail = newNode
        self.size += 1

    # given a node get the node at that index
    def getNodeAtIndex(self, index):
        node = self.head
        if index > self.size:
            raise IndexError("Index out of bounds")
        i = 1
        while index <= self.size:
            if i == index:
                return node
            else:
                node = node.next
                i += 1

    def __iter__(self):
        node = self.head
        index = 0
        while index < self.size:
            yield node.next
            index += 1

    def printList(self):
        d = list()
        node = self.head
        index = 0
        while index < self.size:
            d.append(node.data)
            node = node.next
            index += 1
        print([item for item in d])

    def insertNode(self, newNode, location):

        # if location is greater by 1 or more than the size of the list invalid position to insert
        if location > self.size + 1:
            raise ValueError("Invalid position")

        # inserting at first position when there are more than one elements in that list
        if location == 1:
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode
            self.size += 1

        # inserting at the last position
        elif location == self.size + 1:
            newNode.prev = self.tail
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

        # inserting anywhere else i.e not the first or last position
        else:
            # find the element where the newNode needs to be inserted
            currentNode = self.getNodeAtIndex(location)
            newNode.next = currentNode
            newNode.prev = currentNode.prev
            newNode.prev.next = newNode
            currentNode.prev = newNode
            self.size += 1

    def deleteItem(self, location):

        # if location is greater by 1 or more than the size of the list invalid position to insert
        if location > self.size + 1:
            raise ValueError("Invalid position")

        # delete item at the first position
        if location == 1:
            self.head = self.head.next
            self.head.next.prev = None
            self.size -= 1

        # delete item at the last position
        if location == self.size:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

        # delete item in between
        delNode = self.getNodeAtIndex(location)
        delNode.prev.next = delNode.next
        delNode.next.prev = delNode.prev
        self.size -= 1


if __name__ == "__main__":

    n1 = DNode(1)
    n2 = DNode(2)
    n3 = DNode(3)
    n4 = DNode(4)
    n5 = DNode(5)
    n6 = DNode(6)
    n7 = DNode(7)
    n8 = DNode(8)
    n9 = DNode(9)
    n10 = DNode(10)

    d = DoublyLinkedList(n1)
    d.addNode(n2)
    d.addNode(n3)
    d.addNode(n4)
    d.addNode(n5)
    d.insertNode(n6, 1)
    d.insertNode(n7, 7)
    d.insertNode(n8, 4)
    d.insertNode(n9, 6)
    d.insertNode(n10, 8)
    d.printList()
    d.deleteItem(1)
    d.printList()
    d.deleteItem(8)
    # d.deleteItem(5)
    d.printList()

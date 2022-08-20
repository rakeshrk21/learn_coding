from academy.data_structures.node.node import Node


class SLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def get_size(self):
        return self.size

    def add_node(self, data):
        self.size += 1
        return Node(data)

    def traverse_sll(self):
        node = self.head
        while node:
            print(node)
            node = node.next

    def search_sll(self, ele):
        node = self.head
        index = 0
        while node:
            if ele.data == node.data:
                print(node)
                print(f'element with value {ele.data} found at index {index}')
                return index
            node = node.next
            index += 1
        print("node not found in the linked list")

    def del_item_from_sll(self, node):
        index = self.search_sll(node)
        tempNode = self.head
        # if the element is at the first index
        if index == 0:
            self.head = self.head.next
            return tempNode
        elif index == self.size-1:
            tempNode = self.tail
            self.tail = self.tail.next
            return tempNode
        else:
            while index < self.size - 1:
                lastNode = tempNode
                tempNode = tempNode.next
                if tempNode.data == node.data:
                    lastNode.next = tempNode.next
                    break
            return tempNode

    def insert_item(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        elif location == 1:
            newNode.next = self.head
            self.head = newNode

        elif location == self.size-1:
            newNode.next = None
            self.tail.next = newNode  # tail is pointing to the last node
            self.tail = newNode

        else:
            tempNode = self.head
            index = 0
            print(tempNode, f", Index {index}")
            while index < self.size-1:
                lastNode = tempNode
                tempNode = tempNode.next
                index += 1
                print(tempNode, f", Index {index}")
                if index == location:
                    lastNode.next = newNode
                    newNode.next = tempNode
                    break
        return newNode


sLinkedList = SLinkedList()
node1 = sLinkedList.add_node(1)
node2 = sLinkedList.add_node(2)
node3 = sLinkedList.add_node(3)
node4 = sLinkedList.add_node(4)
node5 = sLinkedList.add_node(5)
node6 = sLinkedList.add_node(6)
node7 = sLinkedList.add_node(7)
print(f'size of the singly linkedlist is {sLinkedList.size}')
sLinkedList.head = node1       # object reference
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
sLinkedList.tail = node7
sLinkedList.tail = node3
print([item.data for item in sLinkedList])
print(sLinkedList.get_size())
node25 = sLinkedList.insert_item(25, 5)
print([item.data for item in sLinkedList])
sLinkedList.traverse_sll()
print(sLinkedList.search_sll(node4))
sLinkedList2 = SLinkedList()
print(sLinkedList2.search_sll(node4))
print(sLinkedList.del_item_from_sll(node1))
print([item.data for item in sLinkedList])
print(sLinkedList.del_item_from_sll(node7))
print([item.data for item in sLinkedList])
print(sLinkedList.del_item_from_sll(node25))
print([item.data for item in sLinkedList])
print(sLinkedList.del_item_from_sll(node5))
print([item.data for item in sLinkedList])
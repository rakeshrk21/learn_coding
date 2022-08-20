from academy.data_structures.node.node import Node
from academy.data_structures.linked_lists.linked_list import SLinkedList

#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next


# creating a queue with linked list data structure
class Queue:
    def __init__(self):
        self.ll = SLinkedList()
        self.size = 0

    def enqueue(self, value):
        newNode = Node(value)

        # if the Queue is empty then
        if self.ll.head is None:
            self.ll.head = newNode
            self.ll.tail = newNode
            self.size += 1
        else:
            self.ll.tail.next = newNode
            self.ll.tail = newNode
            self.size += 1

    def __str__(self):
        values = [str(node) for node in self.ll]
        return ' '.join(values)

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def dequeue(self):
        # remove the first element from the linked list. Queue operates on FIFO principle
        if self.isEmpty():
            return "The queue is empty"
        else:
            tempNode = self.ll.head

            # condition 1: there is only one node in the linked list
            # set head and tail reference to None
            if self.size == 1:
                self.ll.head = None
                self.ll.tail = None

            # condition 2: more than one node exists in the linked list
            else:
                self.ll.head = self.ll.head.next
                self.size -= 1

            return tempNode

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.ll.head


if __name__ == "__main__":
    myQueue = Queue()
    myQueue.enqueue(5)
    myQueue.enqueue(4)
    myQueue.enqueue(6)
    myQueue.enqueue(7)
    myQueue.enqueue(3)
    print(myQueue)
    myQueue.dequeue()
    print(myQueue)
    print(myQueue.peek())



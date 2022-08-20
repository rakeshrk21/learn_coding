class CircularQueue(object):

    def __init__(self, size):
        self.items = [None for _ in range(0, size)]
        self.top = -1
        self.start = -1
        self.maxSize = size

    def enqueue(self, element):
        if self.isFull():
            print("the circular items is full!")
        else:
            if self.isEmpty():
                self.start += 1
                self.top += 1
                self.items[self.top] = element
            elif self.top + 1 == self.maxSize:
                self.top = 0
                self.items[self.top] = element
            else:
                self.top += 1
                self.items[self.top] = element
        return "Element inserted at the end of the items"

    def dequeue(self):
        if self.isEmpty():
            print("the circular items is empty!")
        else:
            element = self.items[self.start]
            start = self.start
            # for last element, start and top will both point to same el
            if self.start == self.top:
                self.start = -1
                self.top = -1
            # if start reaches the max size of the items, set the start = 0
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return element

    def isFull(self):
        if self.start == self.top + 1:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.start == -1:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty():
            return "The circular queue is empty!"
        else:
            return self.items[self.start]

    def __str__(self):
        values = [str(item) for item in self.items]
        return ' '.join(values)

if __name__ == "__main__":
    myQueue = CircularQueue(5)
    myQueue.enqueue(5)
    print(myQueue)
    print('*' * 20)
    myQueue.enqueue(20)
    print(myQueue)
    print('*' * 20)
    myQueue.enqueue(210)
    print(myQueue)
    print('*' * 20)
    myQueue.enqueue(270)
    print(myQueue)
    print('*' * 20)
    myQueue.enqueue(320)
    print(myQueue)
    print('*' * 20)
    myQueue.enqueue(420)
    print(myQueue)
    print('*' * 20)
    myQueue.dequeue()
    print(myQueue)
    print('*' * 20)
    myQueue.enqueue(420)
    print(myQueue)
    print('*' * 20)
    myQueue.enqueue(35)
    print(myQueue)
    print('*' * 20)
    print(myQueue.peek())
    print('*' * 20)
    myQueue.dequeue()
    print(myQueue)
    print('*' * 20)
    myQueue.dequeue()
    print(myQueue)
    print('*' * 20)
    myQueue.dequeue()
    print(myQueue)
    print('*' * 20)
    myQueue.dequeue()
    print(myQueue)
    print('*' * 20)
    print(myQueue.peek())
    print('*' * 20)
    myQueue.dequeue()
    print(myQueue)
    print('*' * 20)
    myQueue.dequeue()
    print(myQueue)
    print('*' * 20)
    myQueue.enqueue(555)
    print(myQueue)
    print('*' * 20)
    print(myQueue.peek())
    print('*' * 20)
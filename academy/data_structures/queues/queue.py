class Queue:

    def __init__(self):
        self.items = list()

    def __str__(self):
        return f'{self.items} is the queue'

    def enqueue(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def dequeue(self):
        if not self.is_empty():
            temp = self.items[0]
            self.items.remove(temp)
            return temp


if __name__ == "__main__":
    myQueue = Queue()
    myQueue.enqueue("hello")
    myQueue.enqueue("this")
    myQueue.enqueue("is")
    myQueue.enqueue("a")
    myQueue.enqueue("test")
    myQueue.enqueue("howdy")
    myQueue.enqueue("hola")

    print(myQueue)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.peek())
    print(myQueue)

    print(len([None for _ in range(0, 5)]))
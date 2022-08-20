from academy.data_structures.queues.QueueLinkedList import Queue


class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def pre_order_traversal(node):
    if not node:
        return
    print(node)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


def in_order_traversal(node):
    if not node:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)


def post_order_traversal(node):
    if not node:
        return
    in_order_traversal(node.left)
    in_order_traversal(node.right)
    print(node.data)


def level_order_traversal(rootNode):
    if not rootNode:
        return
    else:
        # using the queue data structure for traversal which is implemented with linkedList
        q = Queue()
        q.enqueue(rootNode)
        while not(q.isEmpty()):
            root = q.dequeue()
            print(root.data.data)
            if root.data.left is not None:
                q.enqueue(root.data.left)
            if root.data.right is not None:
                q.enqueue(root.data.right)
    return


def search(rootNode, nodeValue):
    found = False
    if not rootNode:
        return found

    # Queue data structure is best suited for level order T
    q = Queue()
    # put the node element in the queue
    q.enqueue(rootNode)

    while not(q.isEmpty()):
        # dequeue the element and check if data matches
        node = q.dequeue()
        print(f'Node element with value {node.data.data} was just removed from the queue')
        if node.data.data == nodeValue:
            print(f'{nodeValue} was found')
            found = True

        if node.data.left is not None:
            q.enqueue(node.data.left)

        if node.data.right is not None:
            q.enqueue(node.data.right)

    return found


def insert(rootNode, nodeValue):
    newNode = BinaryTree(nodeValue)
    if rootNode is None:
        rootNode = newNode
        return "Successfully inserted"
    else:
        q = Queue()
        q.enqueue(rootNode)
        while not(q.isEmpty()):
            node = q.dequeue()

            # check if the left child is vacant
            if node.data.left is not None:
                q.enqueue(node.data.left)
            else:
                node.data.left = node
                return "Successfully inserted as left child"

            # check if the right child is vacant
            if node.data.right is not None:
                q.enqueue(node.data.right)
            else:
                node.data.right = node
                return "Successfully inserted as right child"

def deleteNode(rootNode, dnode):
    if rootNode is None:
        return "The tree is empty"

    else:
        q = Queue()
        q.enqueue(rootNode)
        while not(q.isEmpty()):
            root = q.dequeue()
            if root.data is dnode:
                print(f'deleting the node with data {dnode.data} ')
                root.data = None
                return f'Successfully deleted {rootNode.data.data}'
            if root.data.left is not None:
                if root.data.left is dnode:
                    print(f'deleting the node with data {dnode.data} ')
                    root.data.left = None
                else:
                    q.enqueue(root.data.left)
            if root.data.right is not None:
                if root.data.right is dnode:
                    print(f'deleting the node with data {dnode.data} ')
                    root.data.right = None
                else:
                    q.enqueue(root.data.right)


if __name__ == "__main__":

    root = BinaryTree("Drinks")
    l_hot = BinaryTree("Hot")
    r_cold = BinaryTree("Cold")
    root.left = l_hot
    root.right = r_cold

    l_hot_coffee = BinaryTree("Hot Coffee")
    r_hot_tea = BinaryTree("Hot Tea")
    l_hot.left = l_hot_coffee
    l_hot.right = r_hot_tea

    l_cold_coffee = BinaryTree("Cold Coffee")
    r_cold_tea = BinaryTree("Cold Tea")
    r_cold.left = l_cold_coffee
    r_cold.right = r_cold_tea

    print("-" * 10)
    print("Pre order traversal")
    pre_order_traversal(root)
    print("-" * 10)
    print("In order traversal")
    in_order_traversal(root)
    print("-" * 10)
    print("Post order traversal")
    post_order_traversal(root)
    print("-" * 10)
    print("Level order traversal")
    level_order_traversal(root)
    print(search(root, "Cold Tea"))
    print("-" * 10)
    print(insert(root, "Cappuccino"))
    print(insert(root, "Americano"))
    print(insert(root, "Black Tea"))
    print(insert(root, "Green Tea"))
    print(deleteNode(root, r_cold_tea))
    print("-" * 10)
    level_order_traversal(root)

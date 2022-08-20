from academy.data_structures.queues.queue import Queue

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.data}'


def insertBST(rootNode, value):
    if rootNode.data is None:
        rootNode.data = value
    if value > rootNode.data:
        if rootNode.right is None:
            rootNode.right = BST(value)
        else:
            insertBST(rootNode.right, value)
    else:
        if rootNode.left is None:
            rootNode.left = BST(value)
        else:
            insertBST(rootNode.left, value)


def level_order_traversal(rootNode):
    if rootNode is None:
        return
    q = Queue()
    q.enqueue(rootNode)
    while not(q.is_empty()):
        node = q.dequeue()
        print(node)
        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)


def find(rootNode, value):

    if rootNode.data == value:
        print("found")
    elif value < rootNode.data:
        if rootNode.left.data == value:
            print("found")
        else:
            find(rootNode.left, value)
    else:
        if rootNode.right.data == value:
            print("found")
        else:
            find(rootNode.right, value)

# def deleteNode(rootNode, value):
#
#     # the node to be deleted does not have children or is a leaf node
#     if rootNode.data == value:
#         if rootNode.left is None and rootNode.right is None:
#             rootNode = None
#     else:
#         tempNode = rootNode
#         if value > rootNode.data:
#             if rootNode.right.data == value:
#                 if rootNode.right.right is not None or rootNode.right.left is not None:
#
#         else:
#             deleteNode(rootNode.left, value)
#
#     # the node to be deleted has one child
#
#     # the node to be deleted has two children


if __name__ == "__main__":
    root = BST(70)
    insertBST(root, 50)
    insertBST(root, 90)
    insertBST(root, 30)
    insertBST(root, 60)
    insertBST(root, 20)
    insertBST(root, 40)
    insertBST(root, 80)
    insertBST(root, 100)
    level_order_traversal(root)
    print("search", find(root, 40))
    deleteNode(root, 100)
    level_order_traversal(root)

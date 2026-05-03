from collections import deque
from academy.interview_prep_062025.binary_tree.binary_tree_node import BinaryTreeNode

class BinaryTree:
    def __init__(self, node: BinaryTreeNode):
        self.root = node

    def dfs(self, root):
        if self.root is None:
            return
        self.dfs(root.left)
        self.dfs(root.right)
        return

    def bfs_insert(self, node: BinaryTreeNode):
        if self.root is None:
            self.root = node
        q = deque([self.root]) # queue maintains the insertion order
        while q:
            n = q.popleft()
            if n.left is None:
                n.left = node
                return
            elif n.right is None:
                n.right = node
                return
            q.append(n.left)
            q.append(n.right)

    def bfs_insert_with_array(self, a): # [1,2,3,4,5]
        if not a:
            return
        q = deque()
        q.append(BinaryTreeNode(a[0]))
        for i in range(1, len(a)):
            new_Node = BinaryTreeNode(a[i])
            node = q.popleft()

            if node.left is None:
                node.left = new_Node
                q.append(node.left)
            elif node.right is None:
                node.right = new_Node
                q.append(node.right)


    def bfs_insert_with_array_correct(self, a):
        if not a:
            return
        q = deque()
        q.append(a[0])
        i = 1
        while q and i < len(a) :
            node = q.popleft()
            newNode = BinaryTreeNode(a[i])
            if node.left is None:
                node.left = newNode
                q.append(node.left)
            elif node.right is None:
                node.right = newNode
                q.append(node.right)
            i = i+1



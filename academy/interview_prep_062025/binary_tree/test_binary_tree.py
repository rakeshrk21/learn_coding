from collections import deque
from academy.interview_prep_062025.binary_tree.binary_tree import BinaryTree
from academy.interview_prep_062025.binary_tree.binary_tree_node import BinaryTreeNode

def pre_order_traversal(node: BinaryTreeNode):
    if node is None:
        return
    print(node)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return


def in_order_traversal(node: BinaryTreeNode):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)
    return


def post_order_traversal(node: BinaryTreeNode):
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)


def bfs(node: BinaryTreeNode):
    if node is None:
        return
    q = deque([node])
    while q:
        n = q.popleft()
        print(n.data)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)


def max_depth_bt(rootNode: BinaryTreeNode):
    maxDepth = 0

    if rootNode is None:
        return maxDepth

    def dfs(node: BinaryTreeNode, tempDepth):
        nonlocal maxDepth

        if maxDepth < tempDepth:
            maxDepth = tempDepth

        if node.left:
            print(f'temp depth is {tempDepth}')
            dfs(node.left, tempDepth + 1)

        if node.right:
            dfs(node.right, tempDepth + 1)

    dfs(rootNode, 1)
    return maxDepth

def print_all_paths(node: BinaryTreeNode, path, paths):

    if not node:
        return

    path.append(node.data)

    if not node.left and not node.right:
        paths.append(path.copy())
        path.pop()
        return
    else:
        print_all_paths(node.left, path, paths)
        print_all_paths(node.right, path, paths)

    return paths

def find_max_difference(paths):
    max_difference = 0

    for path in paths:
        path.sort()
        if len(path) > 2:
            temp =  path[len(path)-1]- path[0]
        else:
            temp = path[0]
        if max_difference < temp:
            max_difference = temp
        print(paths)
    return max_difference

def find_max(node: BinaryTreeNode):
    if node is None:
        return
    max_val = 0
    q = deque()
    q.append(node)
    while q:
        n = q.popleft()
        if n.data > max_val:
            max_val = n.data
        if n.right:
            q.append(n.right)
        if n.left:
            q.append(n.left)
    return max_val

def tree_diameter(root: BinaryTreeNode):
    diameter = [0]  # use list so it’s mutable inside dfs

    def dfs(node: BinaryTreeNode):
        if node is None:
            return 0  # height of empty subtree is 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        # diameter through this node
        diameter[0] = max(diameter[0], left_height + right_height)

        # return height of this node
        return 1 + max(left_height, right_height)

    dfs(root)
    return diameter[0]

def max_depth(root: BinaryTreeNode):
    max_depth = [0]

    def dfs(node: BinaryTreeNode, depth):
        # base
        if node is None:
            return depth

        max_depth[0] = max(max_depth[0], depth)

        dfs(node.left, depth+1)
        dfs(node.right, depth+1)

    dfs(root, 1)
    return max_depth[0]

if __name__ == "__main__":
    node = BinaryTreeNode(25)
    binaryTree = BinaryTree(node)
    binaryTree.bfs_insert(BinaryTreeNode(45))
    binaryTree.bfs_insert(BinaryTreeNode(20))

    binaryTree.bfs_insert(BinaryTreeNode(21))
    binaryTree.bfs_insert(BinaryTreeNode(31))

    binaryTree.bfs_insert(BinaryTreeNode(50))
    binaryTree.bfs_insert(BinaryTreeNode(40))

    # bfs(node)
    print(max_depth(node))
    # paths = print_all_paths(node, [], [])
    # print(paths)
    # print(find_max_difference(paths))
    # print(find_max(node))
    # print(max_diff(binaryTree))
    # print(tree_diameter(node))

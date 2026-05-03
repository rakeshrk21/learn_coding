#
# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
#
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
from academy.interview_prep_062025.binary_tree.binary_tree import BinaryTree
from academy.interview_prep_062025.binary_tree.binary_tree_node import BinaryTreeNode


def max_diff(bt: BinaryTree ):


    def dfs(node, path):

        if node is None:
            if len(path)>1:
                sorted_path = sorted(path)
                return abs(sorted_path[0] - sorted_path[len(path)-1])
            else:
                return 0

        # include current node in the path
        new_path = path + [node.data]
        left_max = dfs(node.left, new_path )
        right_max = dfs(node.right, new_path)

        return max(left_max, right_max)

    if not bt.root:
        return 0

    return dfs(bt.root, [])
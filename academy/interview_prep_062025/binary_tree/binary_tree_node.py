class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # get data
    def get_data(self):
        return self.data

    # get left node
    def get_left_node(self):
        return self.left

    #get right node
    def get_right_node(self):
        return self.right

    # set data
    def set_data(self, data):
        self.data = data

    def __str__(self):
        print(self.data)
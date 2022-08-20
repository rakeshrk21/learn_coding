class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+2)
        return ret


tree = TreeNode("Drinks")

cold = TreeNode("Cold")
hot = TreeNode("Hot")
tree.add_child(cold)
tree.add_child(hot)
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
cola = TreeNode("Cola")
fanta = TreeNode("Fanta")
hot.add_child(tea)
hot.add_child(coffee)
cold.add_child(cola)
cold.add_child(fanta)
americano = TreeNode("Americano")
cappuchino = TreeNode("Cappuchino")
green = TreeNode("Green Tea")
black = TreeNode("Black Tea")
coffee.add_child(americano)
coffee.add_child(cappuchino)
tea.add_child(green)
tea.add_child(black)
print(tree)

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
            
        return level


    def print_tree(self):

        level = self.get_level()
        spaces = ' ' * level
        if level:
            spaces += spaces + '|_'
            
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

        


root = TreeNode("1")

node2 = TreeNode("2")
root.add_child(node2)

node3 = TreeNode("3")
root.add_child(node3)

nodea = TreeNode("a")
nodeb = TreeNode("b")

node2.add_child(nodea)
node2.add_child(nodeb)

root.print_tree()

print(root.get_level())
print(node2.get_level())
print(nodeb.get_level())

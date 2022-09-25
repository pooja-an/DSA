class BinaryTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def inorder_print(self):
        nodes = []
        if self.left:
            nodes += self.left.inorder_print()
            
        nodes.append(self.data)

        if self.right:
            nodes += self.right.inorder_print()

        return nodes

    def preorder_print(self):
        nodes = []
        
        nodes.append(self.data)
        
        if self.left:
            nodes += self.left.preorder_print()

        if self.right:
            nodes += self.right.preorder_print()

        return nodes
    
    def postorder_print(self):
        nodes = []
        if self.left:
            nodes += self.left.postorder_print()
        if self.right:
            nodes += self.right.postorder_print()
        nodes.append(self.data)

        return nodes

    def levelorder_print(self):
        q = [] 
        data_items = [] #[10,20,30,40,50]

        q.append(self)

        while len(q) > 0:
            node = q.pop(0)
            data_items.append(node.data)
        
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return data_items

    def height(self):
        if self.left == None and self.right == None:
            return 0
        left_height = self.left.height()
        right_height = self.right.height()

        return 1 + max(left_height, right_height)

    def size(self):
        q = [] 
        data_items = 0 

        q.append(self)

        while len(q) > 0:
            node = q.pop(0)
            data_items += 1
        
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return data_items

    def insert(self, val):
        if val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinaryTree(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinaryTree(val)
        

root = BinaryTree(10)
root.left = BinaryTree(20)
root.right = BinaryTree(30)
root.left.left = BinaryTree(40)
root.left.right = BinaryTree(50)

print("In-order Print:: ",root.inorder_print())
print("Pre-order Print:: ",root.preorder_print())
print("Post-order Print:: ",root.postorder_print())
print("Level-order Print:: ",root.levelorder_print())
print("Height of tree is:: ",root.height())
print("Size of tree is:: ",root.size())

tree = BinaryTree(51)
values = [50,20,10,55,60]
for val in values:
    tree.insert(val)

print("Level-order Print:: ",tree.levelorder_print())


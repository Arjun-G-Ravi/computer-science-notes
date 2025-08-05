class BinaryTree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def _get_level(self):
        level = 0
        node =self
        while node.parent:
            node = node.parent
            level += 1
        return level
    
    def __repr__(self):
        return f'[BinaryTree Object] Val:{self.val}\n{(self._get_level()+1)*"    "}- Left:{self.left}\n{(self._get_level()+1)*"    "}- Right:{self.right}'
    
    def add_left(self, val):
        self.left = BinaryTree(val)
        self.left.parent = self

    def add_right(self, val):
        self.right = BinaryTree(val)
        self.right.parent = self

root = BinaryTree(5)
root.add_left(3)
root.add_right(5)
root.left.add_left(2)
root.right.add_left(0)
root.left.left.add_right(1)
root
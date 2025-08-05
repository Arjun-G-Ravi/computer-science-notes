class Tree:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

    def __repr__(self):
        return f'<Tree obj:Val={self.val}, Children={self.children}'
tree = Tree(5,[Tree(4,[Tree(3)]), Tree(10,[Tree(6), Tree(1,[Tree(100)])])])
tree
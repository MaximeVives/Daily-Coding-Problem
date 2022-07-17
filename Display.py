class Display:
    def __init__(self, tree, count) -> None:
        self.tree = tree
        self.count = [count]

    def print2DUtil(self, root, space) :
        # Base case
        if (root == None) :
            return
    
        # Increase distance between levels
        space += self.count[0]
    
        # Process right child first
        self.print2DUtil(root.right, space)
    
        # Print current node after space
        # count
        print()
        for i in range(self.count[0], space):
            print(end = " ")
        print(root.current)
    
        # Process left child
        self.print2DUtil(root.left, space)

    def print2D(self) :
     
        # space=[0]
        # Pass initial space count as 0
        self.print2DUtil(self.tree, 0)



    
from Display import Display
from Node import Node


exemple_bst_true = Node(8, 
Node(10, Node(14, None, Node(13)), None), 
Node(3, Node(6, Node(7), Node(4)), Node(1))
)

exemple_bst_false = Node(8,
Node(3, Node(6, Node(7), Node(4)), Node(1)), 
Node(10, Node(14, None, Node(13)), None)
)

exemple_bst_empty = None

exemple_bst_unique = Node(8)

# right branch is bigger or equal than parent and left branch is lower than parent

def isBSTValid(node, root=False):
    rightvalid = None
    leftvalid = None

    if node == None and not root:
        return True
    elif node == None and root:
        return False 

    isEndRight = True if (node.right == None) else False
    isEndLeft = True if (node.left == None) else False

    if isEndRight and isEndLeft:
        return True
    else :
        # print(f"curr: {node.current}", end=", ")
        if not isEndRight:
            # print(f"right: {node.right.current}", end=", ")
            if node.right.current >= node.current :
                rightvalid = True
            else:
                rightvalid = False
            
        if not isEndLeft:
            # print(f"left: {node.left.current}", end=", ")
            if node.left.current < node.current :
                leftvalid = True
            else:
                leftvalid = False
        # print("")
    
        if rightvalid == None and leftvalid == None:
            return True
        elif (rightvalid and leftvalid == None) or (rightvalid==None and leftvalid) or (rightvalid and leftvalid):
            return isBSTValid(node.left) and isBSTValid(node.right)
        elif (not rightvalid and leftvalid == None) or (rightvalid==None and not leftvalid) or (not rightvalid and not leftvalid):
            return False


# printer = Display(exemple_bst, 10)
# printer.print2D()

print(isBSTValid(exemple_bst_true, root=True))  # Expected : True
print(isBSTValid(exemple_bst_unique, root=True)) # Expected : True
print(isBSTValid(exemple_bst_false, root=True)) # Expected : False
print(isBSTValid(exemple_bst_empty, root=True)) # Expected : False


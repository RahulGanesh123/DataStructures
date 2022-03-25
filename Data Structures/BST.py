#
# What is a binary search tree?
    # 1) A binary search tree is basically a tree of interconnected nodes, where all the nodes on the left of a node are less than it, and all the nodes on the right of the node are greater than it
    # 2) Similar to the linked list where the starting point is often referred to as the head of the list, the 1st node in the binary search tree is referred to as the root or parent node of the tree
    # 3) All elements in a BST are unique, like the set() method.
# How does a BST look like?
#                                           7
#                                         /   \
#                                        3     12
#                                       / \     \
#                                      2   5     18
#                                        \        \
#                                         4        22
# As one can see, all nodes to the left of any node are less than that node and all elements to the right of the node are greater than it
# 
# Pros of BST:
# 1) Searching and inserting elements takes (O log n) which is extremely fast
#    a) What does this mean you may ask?
#       i) Lets take a BST of size 8. From the root node, you can immediately tell if an element is on the left/right of it, so that effectively eliminates half the nodes
#       ii) Repeat this until you find the element. So if you have 8 elements, u go from  8 --> 4 --> 2 --> 1


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def addNodes(self, data):
        if self.data == data: # checks if the value you are passing is already in the BST. Think about it, since you are using recursion, you will be able to check if any node is already equal to the value
            return
        elif self.data == None:
            self.data = BinarySearchTree(data)
        elif data < self.data:
            if self.left == None:
                self.left = BinarySearchTree(data)
            else:
                self.left.addNodes(data)
                 #This is just recursion. Basically, if there is already a subtree in the BST, keep on traversing it until u find self.left == None. If that is the case, then u add the new data to the BST
                 #Also remember that recursion involves going through the entire method, that is, all the conditions are checked for each node
        elif data > self.data:
            if self.right == None:
                self.right = BinarySearchTree(data)
            else:
                self.right.addNodes(data)

    
    def search(self, val):
        if self.data == val:
            return True
        elif val < self.data:
            if self.left == None:
                return False
            else:
                return self.left.search(val) # Basically, this recursion keeps on running the search in the left part of the tree and if it finds the value, return true, else false.
        elif val > self.data:
            if self.right == None:
                return False
            else:
                return self.right.search(val) 

    def getMinVal(self):
        if self.data == None:
            return -1 #signifies empty list
        elif self.left:
            if self.left == None:
                return self.data
            else:
                self.left.getMinVal()

    def getMaxVal(self):
        if self.data == None:
            return -1
        elif self.right:
            if self.right == None:
                return self.data
            else:
                self.right.getMaxVal()

    def sum(self):
        sumTree = 0
        if self.data == None:
            return 0
        if self.left:
            sumTree+=self.left.sum()
        sumTree+=self.data
        if self.right:
            sumTree+=self.right.sum()
        return sumTree


    def sortTree(self):
        sort = []
        if self.data == None:
            return -1
        if self.left:
            sort+=self.left.sortTree()
        sort+=self.data
        if self.right:
            sort+=self.right.sortTree()
        return sort

                                 
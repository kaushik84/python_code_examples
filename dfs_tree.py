class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def printInorder(root):

    if root:
        printInorder(root.left)
        print(root.value)
        printInorder(root.right)

def printPreorder(root):

    if root:
        print(root.value)
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):

    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.value)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

    if lheight > rheight:
         return lheight + 1
    else:
        return rheight + 1

def printGivenLevel(node, level):
    if node is None:
        return
    if level == 1:
        print(node.value)
    elif level > 1:
        printGivenLevel(node.left, level - 1)
        printGivenLevel(node.right, level - 1)




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(8)
root.right.right = Node(9)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)

#printInorder(root)

#printPreorder(root)

#printPostorder(root)
#print(height(root.left))

printGivenLevel(root, 3)

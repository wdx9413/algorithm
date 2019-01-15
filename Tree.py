class Tree:
    head = None
    class Node:
        data = None
        parent = None
        left = None
        right = None
        def __init__(self, data):
            self.data = data
        def __str__(self):
            return str(self.data)
    def __init__(self):
        pass
    def inorder_walk(self):
        if self.head == None:
            print("null")
            return
        def walk(node, walk):
            if node != None:
                walk(node.left, walk)
                print(node)
                walk(node.right, walk)
        node = self.head
        walk(node, walk)
            
    def preoder_walk():
        pass
    def postorder_walk():
        pass
    def min(self, node):
        while node.left != None:
            node = node.left
        return node
    def max(self, node):
        while node.right != None:
            node = node.right
        return node

    def successor(self, node):
        if node.right != None:
            return self.min(node.right)
        nodeP = node.parent
        while nodeP != None and node == nodeP.right:
            node = nodeP
            nodeP = node.parent
        return nodeP
    def pre_successor(self, node):
        if node.left != None:
            return self.max(node.left)
        nodeP = node.parent
        while nodeP != None and node == nodeP.left:
            node = nodeP
            nodeP = node.parent
        return nodeP
    def insertNode(self, data):
        i = self.head
        newNode = self.Node(data)
        if i == None:
            self.head = newNode
            return
        p = i.parent
        while i != None:
            p = i
            if data >= i.data:
                i = i.right
            else :
                i = i.left
        if data >= p.data:
            p.right = newNode
            p.right.parent = p
        else :
            p.left = newNode
            p.left.parent = p

    def deleteNode(self, data):
        n = self.head
        while n != None and n.data != data:
            if data >= n.data:
                n = n.right
            else:
                n = n.left
        if n == None or n.data != data:
            print("hasn't this node")
            return None 
        else:
            self.transparent(n)
            return n
    def transparent(self, node):
        if node.right != None:
            s = self.successor(node)
            if s == s.parent.left:
                s.parent.left = s.right
            else:
                s.parent.right = s.right
            s.parent = node.parent
            if s.parent != None:
                if node == s.parent.left:
                    s.parent.left = s
                else:
                    s.parent.right = s
            else:
                self.head = s
            s.left = node.left
            s.right = node.right
            if node.left != None:
                node.left.parent = s
            if node.right != None:
                node.right.parent = s
        elif node.left != None:
            s = node.left
            s.parent = node.parent
            if s.parent != None:
                if node == s.parent.left:
                    s.parent.left = s
                else:
                    s.parent.right = s
            else:
                self.head = s
        else:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None


        
if __name__ == "__main__":
    tree = Tree()
    tree.insertNode(1)
    tree.insertNode(2)
    tree.insertNode(1.5)
    tree.insertNode(1.5)
    tree.insertNode(3)
    tree.insertNode(3)
    tree.insertNode(3)
    tree.insertNode(0)
    tree.insertNode(0)
    tree.insertNode(0)
    tree.insertNode(-1)
    tree.inorder_walk()
    print("=======")
    tree.deleteNode(3)
    tree.deleteNode(3)
    tree.deleteNode(3)
    tree.deleteNode(3)
    tree.deleteNode(3)
    tree.inorder_walk()


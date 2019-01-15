R = 'red'
B = 'black'
class Node:
    parent = None
    data = None
    left = None
    right = None
    color = None
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return str(self.data)

class Tree:
    def minimum(self, n):
        while n.left != None:
            n = n.left
        return n
    def maximum(self, n):
        while n.right != None:
            n = n.right
        return n 
    def successor(self, n):
        if n.right != None:
            return self.minimum(n.right)
        m = n.parent
        while m != None and n == m.right:
            n = m
            m = m.parent
        return m
    def presuccessor(self, n):
        if n.left != None:
            return self.maximum(n.left)
        m = n.parent
        while m != None and n == m.left:
            n = m
            m = m.parent
        return m
    def left_rotate(self, n):
        r = n.right
        # r left node
        n.right = r.left
        if r.left != None:
            r.left.parent = n
        r.parent = n.parent
        if n.parent != None:
            if n == n.parent.left:
                n.parent.left = r
            else:
                n.parent.right = r
        else:
            self.root = l
        r.left = n
        n.parent = r
    def right_rotate(self, n):
        l = n.left
        n.left = l.right
        if n.left != None:
            n.left.parent = n
        l.parent = n.parent
        if n.parent != None:
            if n == n.parent.left:
                n.parent.left = l
            else:
                n.parent.right = l
        else:
            self.root = l
        l.right = n
        n.parent = l


class RBTree(Tree):
    root = None
    def __init__(self, n=None):
        Tree.__init__(self)
        if n != None:
            self.root = n
    def insert_node(self, n):
        if self.root == None:
            self.root = n
            n.color = B
            return
        t = self.root
        p = t
        while t != None:
            p = t
            if n.data >= t.data:
                t = t.right
            else:
                t = t.left
        if n.data >= p.data:
            p.right = n
        else:
            p.left = n
        n.parent = p
        n.color = R
        self.fix_insert(n)
    def fix_insert(self, n):
        while n.parent != None and n.parent.color == R:
            if n.parent == n.parent.parent.left:
                w = n.parent.parent.right
                if w != None and w.color == R:
                    w.color = B
                    n.parent.color = B
                    n.parent.parent.color = R
                    n = n.parent.parent
                else:
                    if n == n.parent.right:
                        n = n.parent
                        self.left_rotate(n)
                    n.parent.color = B
                    n.parent.parent.color = R
                    self.right_rotate(n.parent.parent)
            else:
                w = n.parent.parent.left
                if w != None and w.color == R:
                    w.color = B
                    n.parent.color = B
                    n.parent.parent.color = R
                    n = n.parent.parent
                else:
                    if n == n.parent.left:
                        n = n.parent
                        self.right_rotate(n)
                    n.parent.color = B
                    n.parent.parent.color = R
                    self.left_rotate(n.parent.parent)
        self.root.color = B
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
    def remove_node(self, z):
        y = z
        color = y.color
        if z.left == None:
            x = z.right
            self.transplant(z, x)
        elif z.right == None:
            x = z.left
            self.transplant(z, x)
        else:
            y = self.maximum(z.right)
            color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, x)
                y.right = z.right 
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if color == B:
            self.fix_remove(x)
            
    def fix_remove(self, x):
        while x != self.root and x.color == B:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == R:
                    w.color = B
                    x.parent.color = R
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == B and w.right.color == B:
                    w.color = R
                    x = x.parent
                else:
                    if w.right.color == B:
                        w.left.color = B
                        w.color = R
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = B
                    w.right.color = B
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == R:
                    w.color = B
                    x.parent.color = R
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == B and w.right.color == B:
                    w.color = R
                    x = x.parent
                else:
                    if w.left.color == B:
                        w.right.color = B
                        w.color = R
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = B
                    w.left.color = B
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = B

    def get_depth(self):
        self.depth = 0
        r = self.root
        def son(son, n, d):
            if n.right == None and n.left == None:
                if d > self.depth:
                    self.depth = d
            else:
                if n.left != None:
                    son(son, n.left, d+1)
                if n.right != None:
                    son(son, n.right, d+1)

        son(son, r, 1)
        return self.depth

t = RBTree()
n1 = Node(2)
n2 = Node(1)
n3 = Node(1)
n4 = Node(3)
n5 = Node(3)
t.insert_node(n1)
t.insert_node(n2)
t.insert_node(n3)
t.insert_node(n4)
t.insert_node(n5)
print(t.root)
print(t.root.left)
print(t.root.right)
print(t.get_depth())
print('======')
t.remove_node(n2)
print(t.root)
print(t.root.left)
print(t.root.right)
print(t.get_depth())


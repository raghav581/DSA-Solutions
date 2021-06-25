class Node:
    val = None
    left = None
    right = None
    def __init__(self, val):
        self.val = val
class Tree:
    root = None
    L = None
    index = None
    def __init__(self, val):
        self.root = val
        self.L = [self.root]
        self.index = 0
    
    def getchild(self, val):
        if self.root is None:
            self.root = val
            self.Index = 0
            self.L = [self.root]
            return
        if self.L[self.index].left is None:
                self.L[self.index].left = val
                self.L.append(self.L[self.index].left)
                return
        if self.L[self.index].right is None:
                self.L[self.index].right = val
                self.L.append(self.L[self.index].right)
                self.index += 1
                return

    def display(self, root):
        if root.left is not None:
            self.display(root.left)
        print(root.val,end =' ')
        if root.right is not None:
            self.display(root.right)

Da, Db = dict(), dict()
tmp = None
def lowestCommonManager(root, One, Two):
    global tmp, Da, Db
    if tmp is None:
        if root.left is not None:
            lowestCommonManager(root.left, One, Two)
            if Da.get(root.left, False):
                Da[root] = True
            if Db.get(root.left, False):
                Db[root] = True
        if root.right is not None:
            lowestCommonManager(root.right, One, Two)
            if Da.get(root.right, False):
                Da[root] = True
            if Db.get(root.right, False):
                Db[root] = True
        if root.val == One.val:
            Da[root] = True
        if root.val == Two.val:
            Db[root] = True
        if Da.get(root, False) and Db.get(root, False) and tmp is None:
            tmp = root
    return tmp

if __name__ == "__main__":
    N = int(input("Enter No. of Nodes for Organisation: "))
    root = Node(input("Enter Node 1: "))
    A = Tree(root)
    for i in range(N - 1):
        A.getchild(Node(input("Enter Node {}: ".format(i+2))))
    one, two = map(Node, input("Enter 2 Quary Nodes: ").split())
    res = lowestCommonManager(A.root, one, two)
    print(res.val)
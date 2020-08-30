#steve su 
#hw1.py
#csci3202
import sys

class Node:
    def __init__(self, key, leftchild, rightchild, parent):
        self.key = key
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.parent = parent
        
    def getChildren(self):
        return [self.leftchild,self.rightchild]  


class Tree:
    def __init__(self, rootkey):
        # Create a new tree while setting root
        self.root = Node(rootkey, None, None, None)

    def checkTree(self, key, root):
        # Recursive function that searches through tree to find
        # if key exists

        if root is None:
            # if there is no root in tree
            return False
        if root.key == key:
            if root.leftchild is None or root.rightchild is None:
                return root
            else:
                return False
        else:
            for child in root.getChildren():
                add_temp = self.checkTree(key, child)
                if add_temp:
                    return add_temp

    # your code goes here
    def add(self, key, parentKey):
        #find parent node by key?
        
        pnode = self.checkTree(parentKey, self.root)
        #print(pnode.key)
        if pnode==None:
            print('parent node not found')
            return
        if pnode.leftchild == None:
            newnode = Node(key,None,None,pnode)
            pnode.leftchild = newnode
            #print(pnode.leftchild.key)
        elif pnode.rightchild == None:
            newnode = Node(key,None,None,pnode)
            pnode.rightchild = newnode
        else: 
            print("error parent's left and right child are full")
            return "Unimplemented method: Node not added"
        
        return
    
    def findNodeDelete(self, key, root):
        if root is None:
            return False
        if key == root.key:
            if root.leftchild is None and root.rightchild is None:
                if root.parent.leftchild.key == key:
                    root.parent.leftchild = None
                elif root.parent.rightchild.key == key:
                    root.parent.rightchild = None
                root = None
                return True
            else:
                print("Node not deleted, has children")
                return False
        else:
            for child in root.getChildren():
                delete_node = self.findNodeDelete(key, child)
                if delete_node:
                    return delete_node

    def delete(self, key):
        if self.root is None:
            self.root = Node(key, None, None, None)
        if key == self.root.key:
            if self.root.leftchild is None and self.root.rightchild is None:
                # print("Deleting Root")
                self.root = None
                return True
            else:
                print("Node not deleted, has children")
                return False
        else:
            for child in self.root.getChildren():
                delete_node = self.findNodeDelete(key, child)
                if delete_node:
                    return delete_node

        print("Parent not found.")
        return False

    def printTree(self):
        if not self.root is None:
            print(self.root.key)
            for child in self.root.getChildren():
                self.printBranch(child)
        else:
            return

    def printBranch(self, root):
        if root is None:
            return
        else:
            print(root.key)
            for child in root.getChildren():
                self.printBranch(child)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        # check if key already exists
        if key in self.vertices:
            print("Vertex already exists")
        else:
            self.vertices[key] = []

    # your code goes here
    def addEdge(self, key1, key2):
        if key1 in self.vertices:
            self.vertices[key1].append(key2)
            print('edge added ', key1, key2)
            #print(self.vertices)
        else:
            print('error-edge could not be created')
        return "Unimplemented Method: Edge not added"

    # your code goes here
    def findVertex(self, key):
        if (key in self.vertices):
            print('vertex ',key,' found')
        else: 
            print('vertex ',key, ' not found')
            return "Unimplemented Method: No vertex found"

'''''''''''''''''''''''''''''''''''''''''''''''''''
Tests
'''''''''''''''''''''''''''''''''''''''''''''''''''

# Tree Test

print("-------------------------------------------")
print("Tree Test")
print("add 10 ints to tree, print In-Order, delete 2 ints, print In-Order")
print("")

tree = Tree(5)
tree.add(6, 5)
tree.add(4, 5)
tree.add(7, 4)
tree.add(3, 7)
tree.add(8, 4)
tree.add(2, 8)
tree.add(9, 7)
tree.add(1, 3)
tree.add(10, 3)

print("")

tree.printTree()

print("")

tree.delete(10)
tree.delete(1)

tree.add(18, 3)

tree.printTree()

# Graph Test

print("-------------------------------------------")
print("Graph Test")
print("Add 10 vertices, make 20 edges, print edges of five vertices")
print("")

g = Graph()
g.addVertex(1)
g.addVertex(11)
g.addVertex(12)
g.addVertex(13)
g.addVertex(14)
g.addVertex(15)
g.addVertex(16)
g.addVertex(17)
g.addVertex(18)
g.addVertex(19)
g.addVertex(100)

g.addEdge(1, 12)
g.addEdge(1, 13)
g.addEdge(11, 14)
g.addEdge(15, 11)
g.addEdge(16, 100)
g.addEdge(15, 17)
g.addEdge(15, 12)
g.addEdge(12, 13)
g.addEdge(12, 14)
g.addEdge(12, 16)
g.addEdge(12, 17)
g.addEdge(1, 100)
g.addEdge(12, 100)
g.addEdge(15, 100)
g.addEdge(19, 12)
g.addEdge(13, 100)
g.addEdge(14, 100)
g.addEdge(100, 19)
g.addEdge(19, 18)
g.addEdge(19, 17)
g.addEdge(52, 53)

g.findVertex(1)
g.findVertex(12)
g.findVertex(13)
g.findVertex(14)
g.findVertex(100)
g.findVertex(52)

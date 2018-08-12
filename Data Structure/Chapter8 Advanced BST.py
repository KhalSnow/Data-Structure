# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:21:38 2018

@author: wyh
"""

#Splay tree
import random
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return ("node[%s]" % self.val)
class BinaryTree(object):
    def __init__(self):
        self.root = None
    def insert(self, val, parent = None):
        if parent == None:
            parent = self.root
        if parent == None:
            self.root = Node(val)
            return
        elif val < parent.val:
            if parent.left is None:
                parent.left = Node(val)
                return
            else:
                self.insert(val, parent.left)
        else:
            if parent.right is None:
                parent.right = Node(val)
                return
            else:
                self.insert(val, parent.right)
    def search(self, val, node = None):
        if node is None:
            node = self.root
        if node is None:
            return None
        elif val == node.val:
            return node
        elif val < node.val:
            if node.left is not None:
                leftrv = self.search(val, node.left)
                if leftrv is not None:
                    return leftrv
        elif val > node.val:
            if node.right is not None:
                rightrv = self.search(val, node.right)
                if rightrv is not None:
                    return rightrv
        return None
    def inorder_traverse(self, root):
        if root == None:
            return 
        self.inorder_traverse(root.left)
        print(root.val, end = '\n')
        self.inorder_traverse(root.right)

class SplayTree(object):
    def __init__(self):
        self.root = None
    def insert(self, val, parent = None):
        if parent == None:
            parent = self.root
        if parent == None:
            self.root = Node(val)
            return
        elif val < parent.val:
            if parent.left is None:
                parent.left = Node(val)
                return
            else:
                self.insert(val, parent.left)
        else:
            if parent.right is None:
                parent.right = Node(val)
                return
            else:
                self.insert(val, parent.right)
    def search(self, val, node = None, p = None, g = None, gg = None):
        if node is None:
            node = self.root
        if node is None:
            return None
        elif val == node.val: #splay
            if p is not None:
                if g is None:
                    self.rotateup(node, p, g)
                elif ((g.left == p and p.left == node) or
                      (g.right == p and p.right == node)):
                    #Zig-zig: swap parent with grandparent
                    self.rotateup(p, g, gg)
                    #Then swap node with parent
                    self.rotateup(node, p, gg)
                else:
                    # Zig-zag: swap node with parent
                    self.rotateup(node, p, g)
                    # Then swap node with grandparent
                    self.rotateup(node, g, gg)
                return node
            elif val < node.val:
                if node.left is not None:
                    leftrv = self.search(val, node.left, p, g)
                    if leftrv is not None:
                        return leftrv
            elif val > node.val:
                if node.right is not None:
                    rightrv = self.search(val, node.right, p, g)
                    if rightrv is not None:
                        return rightrv
            return None
    def rotateup(self, node, parent, g = None):
        if node == parent.left:
            parent.left = node.right
            node.right = parent
            if self.root == parent:
                self.root = node
        elif node == parent.right:
            parent.right = node.left
            node.left = parent
            if self.root == parent:
                self.root = node
        else:
            print("This is impossible. ")
        if g is not None:
            if g.right == parent:
                g.right = node
            elif g.left == parent:
                g.left = node
    def inorder_traverse(self, root):
        if root == None:
            return
        self.inorder_traverse(root.left)
        print(root.val, end = '\n')
        self.inorder_traverse(root.right)

if __name__ == "__main__":
    bt = BinaryTree()
    st = SplayTree()
    array = [random.randint(0,100) for i in range(0,20)]
    for i in array:
        bt.insert(i)
        st.insert(i)
    bt.search(array[10])
    st.search(array[10])
    print("BinaryTree_InorderTraverse: ")
    print(bt.inorder_traverse(bt.root))
    print("SplayTree_InorderTraverse: ")
    print(st.inorder_traverse(st.root))

#B Tree
class BTreeNode(object):
    def __init__(self, leaf = False):
        self.leaf = leaf
        self.keys = []
        self.children = []
    def __str__(self):
        if self.leaf:
            return "Leaf BTreeNode with {0} keys\n\tK:{1}\n\tC:{2}\n".format(len(self.keys), self.keys, self.children)
        else:
            return "Internal BTreeNode with {0} keys, {1} children\n\tK:{2}\n\n".format(len(self.keys), len(self.children), self.keys, self.children)
class BTree(object):
    def __init__(self, t):
        self.root = BTreeNode(leaf = True)
        self.t = t
    def search(self, k, x = None):
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:  # look for index of k
                i += 1
            if i < len(x.keys) and k == x.keys[i]: # found exact match
                return (x, i)
            elif x.leaf: # no match in keys, and is leaf ==> no match exists
                return None
        else: # no node provided, search root of tree
            return self.search(k, self.root) 
    def insert(self, k):
        r = self.root
        if len(r.keys) == (2 * self.t) - 1: # keys are full, so we must split
            s = BTreeNode()
            self.root = s
            s.children.insert(0, r) # former root is now 0th child of new root s
            self.split_children(s, 0)
            self.insert_nonfull(s, k)
        else:
            self.insert_nonfull(r, k)
    def insert_nonfull(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split_children(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_nonfull(x.children[i], k)
    def split_children(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(leaf = y.leaf)
        # slide all children of x to the right and insert z at i
        x.c.insert(i+1, z)
        x.keys.insert(i, y.keys[t-1])
        
        # keys of z are t to 2t - 1,
        # y is then 0 to t-2
        z.keys = y.keys[t : (2 * t - 1)]
        y.keys = y.keys[0 : (t-1)]
        
        # children of z are t to 2t els of y.c
        if not y.leaf:
            z.c = y.c[t : (2 * t)]
            y.c = y.c[0 : (t-1)]    
        
    def __str__(self):
        r = self.root
        return r.__str__() + '\n'.join([child.__str__() for child in r.c]) 
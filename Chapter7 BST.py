# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:49:15 2018

@author: wyh
"""

#Binary Search Tree
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
    def insert(self, root, val):
        while True:
            if self.search(root, val) == True:
                break
            else:
                if root is None:
                    root = Node(val)
                if val < root.val:
                    root.left = self.insert(root.left, val)
                elif val > root.val:
                    root.right = self.insert(root.right, val)
        return root
    def search(self, root, val):
        if root is None:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)
    def delete(self, root, val):
        if root is None:
            return
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else: #找到了val
            if root.left and root.right:
                target = self.minimum(root.right)
                root.val = target.val
                root.right = self.delete(root.right, target.val)
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                root = None
        return root
    def minimum(self, root): #返回最小值的节点。其实就是most left one
        if root.left:
            return self.mimimum(root.left)
        else:
            return root
    def maximum(self, root): #返回最大值的节点。其实就是most right one
        if root.right:
            return self.maximum(root.right)
        else:
            return root
    def print_tree(self, root): #打印二叉搜索树(中序打印，有序数列)
        if root == None:
            return 
        self.print_tree(root.left)
        print(root.val, end = ' ')
        self.print_tree(root.right)
if __name__ == '__main__':
    bst = BST()
    root = Node(3)
    bst.insert(root, 2)
    bst.insert(root, 1)
    bst.insert(root, 4)
    bst.insert(root, 9)
    bst.insert(root, 7)
    bst.print_tree(root)
    print(bst.search(root, 1))
    print(bst.search(root, 4))
    print(bst.search(root, 8))
    bst.delete(root,1)
    print(bst.search(root, 1))
    bst.print_tree(root)


#Adelson-Velsky and Landis Tree
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
class AVLTree(object):
    def __init__(self):
        self.root = None
    #AVL树的查找操作
    def lookup(self, root, val):
        if root is None:
            return False
        if val == root.val:
            return True
        elif val < root.val:
            return self.lookup(root.left, val)
        else:
            return self.lookup(root.right, val)
    def minimum(self, root):
        if root.left:
            return self.minimum(root.left)
        else:
            return root
    def maximum(self, root):
        if root.right:
            return self.maximum(root.right)
        else:
            return root
    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height
    #AVL树的插入操作
    def insert(self, root, val):
        if root is None:
            root = Node(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
            if (self.height(root.left) - self.height(root.right)) == 2:
                if val < root.left.val:
                    root = self.single_left_rotate(root)
                else:
                    root = self.double_left_rotate(root)
        elif val > root.val:
            root.right = self.insert(root.right, val)
            if (self.height(root.right) - self.height(root.left)) == 2:
                if val < root.right.val:
                    root = self.double_right_rotate(root)
                else:
                    root = self.single_right_rotate(root)
        root.height = max(self.height(root.right), self.height(root.left)) + 1
        return root
    def single_left_rotate(self, root):
        k = root.left
        root.left = k.right
        k.right = root
        root.height = max(self.height(root.right), self.height(root.left)) + 1
        k.height = max(self.height(k.left), root.height) + 1
        return k
    def single_right_rotate(self, root):
        k = root.right
        root.right = k.left
        k.left = root
        root.height = max(self.height(root.right), self.height(root.left)) + 1
        k.height = max(self.height(k.right), root.height) + 1
        return k
    def double_left_rotate(self, root):
        root.left = self.single_right_rotate(root.left)
        return self.single_left_rotate(root)
    def double_right_rotate(self, root):
        root.right = self.single_left_rotate(root.right)
        return self.single_right_rotate(root)
    #AVL树的删除操作
    def delete(self, root, val):
        if root is None:
            return
        if val < root.val:
            root.left = self.delete(root.left, val)
            if (self.height(root.right) - self.height(root.left)) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.single_right_rotate(root)
                else:
                    root = self.double_right_rotate(root)
            root.height = max(self.height(root.left), self.height(root.right)) + 1
        elif val > root.val:
            root.right = self.delete(root.right, val)
            if (self.height(root.left) - self.height(root.right)) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.single_left_rotate(root)
                else:
                    root = self.double_left_rotate(root)
            root.height = max(self.height(root.left), self.height(root.right)) + 1
        elif root.left and root.right:
            if root.left.height <= root.right.height:
                min_node = self.minimum(root.right)
                root.val = min_node.val
                root.right = self.delete(root.left, root.val)
            else:
                max_node = self.maximum(root.left)
                root.val = max_node.val
                root.left = self.delete(root.left, root.val)
            root.height = max(self.height(root.left), self.height(root.right)) + 1
        else:
            if root.right:
                root = root.right
            else:
                root = root.left
        return root
    def print_tree(self, root): 
        if root == None:
            return 
        self.print_tree(root.left)
        print(root.val, end = ' ')
        self.print_tree(root.right)
if __name__ == '__main__':
    number_list = (7, 4, 1, 8, 2, 9, 10, 6, 3)
    avl = AVLTree()
    root = Node(5)
    for number in number_list:
        avl.insert(root, number)
    avl.print_tree(root)
    avl.delete(root, 4)
    avl.print_tree(root)
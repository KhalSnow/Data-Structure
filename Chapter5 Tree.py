# -*- coding: utf-8 -*-
"""
Created on Fri May 25 19:40:03 2018

@author: wyh
"""

class Node:
    def __init__(self, item = -1):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree:
    def __init__(self):
        self.root = Node()
        self.queue = []

    def add(self, item):
        node = Node(item)
        if self.root.item == -1:
            self.root = node
            self.queue.append(self.root)
        else:
            treenode = self.queue[0]
            if treenode.lchild is None:
                treenode.lchild = node
                self.queue.append(treenode.lchild)
            else:
                treenode.rchild = node
                self.queue.append(treenode.rchild)
                self.queue.pop(0)
    #层次遍历
    def traverse(self, root):
        if self.root is None:
            return
        queue = []
        res = []
        node = root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            res.append(node.item)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)
        print(res)
    #递归
    #先序遍历
    def preorder_traverse(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder_traverse(root.lchild)
        right_item = self.preorder_traverse(root.rchild)
        return result + left_item + right_item
    #中序遍历
    def inorder_traverse(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder_traverse(root.lchild)
        right_item = self.inorder_traverse(root.rchild)
        return left_item + result + right_item
    #后序遍历
    def postorder_traverse(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder_traverse(root.lchild)
        right_item = self.postorder_traverse(root.rchild)
        return left_item + right_item + result
    #迭代、栈堆
    #先序遍历
    def preorder_stack(self, root):
        if root is None:
            return
        stack = []
        res = []
        node = root
        while node or stack:
            while node:
                res.append(node.item)
                stack.append(node)
                node = node.lchild
            node = stack.pop()
            node = node.rchild
        print(res)
    #中序遍历
    def inorder_stack(self, root):
        if root is None:
            return
        stack = []
        res = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.lchild
            node = stack.pop()
            res.append(node.item)
            node = node.rchild
        print(res)
    #后序遍历
    def postorder_stack(self, root):
        if root is None:
            return
        stack1 = []
        stack2 = []
        res = []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.lchild:
                stack1.append(node.lchild)
            if node.rchild:
                stack1.append(node.rchild)
            stack2.append(node)
        while stack2:
            res.append(stack2.pop().item)
        print(res)

if __name__ == '__main__':
    tree = Tree()
    for i in range(20):
        tree.add(i)
print(tree.traverse(tree.root))
print(tree.preorder_traverse(tree.root))
print(tree.preorder_stack(tree.root))
print(tree.inorder_traverse(tree.root))
print(tree.inorder_stack(tree.root))
print(tree.postorder_traverse(tree.root))
print(tree.postorder_stack(tree.root))
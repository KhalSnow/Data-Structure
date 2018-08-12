# -*- coding: utf-8 -*-
"""
Created on Tue May 22 08:39:10 2018

@author: wyh
"""

class Stack(object):
    #希望限定Stack类的成员只有items
    #__slots__ = ('__items')
    def __init__(self):
        self.items = []
        #希望items[]是Stack的私有属性
        #self.__items = []
    def empty(self):
        return self.items == []
    def top(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
if __name__ == '__main__':
    stack = Stack()
    stack.push('h')
    stack.push('e')
    stack.push('y')
    print(stack.size())
    print(stack.top())
    print(stack.pop())
    print(stack.size())
    print(stack.pop())
    print(stack.pop())
    print(stack.empty())

#进制转换
def convert(stack, n, base):
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E', 'F']
    array = []
    while(n > 0):
        stack.push(digit[n % base])
        n //= base
    while(not stack.empty()):
        array.append(stack.pop())
    print(array)
if __name__ == '__main__':
    stack = Stack()
    print(convert(stack, 2018, 5))
    print(convert(stack, 2018, 16))

#括号匹配
def bracket_match(str):
    open_brackets = '([{<'
    close_brackets = ')]}>'
    brackets_map = {')': '(', ']': '[', '}': '{', '>': '<'} #映射左右括号便于出栈判断
    stack = []
    index = 0
    balanced = True
    while index < len(str) and balanced:
        char = str[index]
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) == 0:
                balanced = False
            elif brackets_map[char] == stack[-1]:
                stack.pop()
            else:
                balanced = False
        index += 1
    if len(stack) == 0 and balanced:
        return True
    else:
        return False
if __name__ == '__main__':
    str1 = '([<^>x[ ]{a}]{/}{t}g<^>)<{x}b>{x}<z({%}w >[b][c[c]]{<h>{h}}'
    print(bracket_match(str1))
    str2 = '(a)[b]{c}<d>'
    print(bracket_match(str2))
    str3 = '(())((()()))'
    print(bracket_match(str3))
    str4 = '(()'
    print(bracket_match(str4))

#栈混洗 Stack permutation

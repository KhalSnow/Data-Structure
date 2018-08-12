# -*- coding: utf-8 -*-
"""
Created on Wed May 16 21:35:15 2018

@author: wyh
"""

#O(n^2)
def delete_duplicated_elements1(array):
    array.sort()
    i = 0
    while i < len(array)-1:
        if array[i] == array[i+1]:
            del array[i+1]
        else:
            i += 1
    return array
if __name__ == '__main__':
    array = [1,2,3,4,2,1,4,5,7,3,5,7,9,3,2,1,4,5,1,1]
    print(delete_duplicated_elements1(array))

#O(n)
def delete_duplicated_elements2(array):
    array.sort()
    i,j = 0,0
    while j < len(array)-1:
        j += 1
        if array[i] != array[j]:
            i += 1
            array[i] = array[j]
    del array[i+1:]
    return array
if __name__ == '__main__':
    array = [1,2,3,4,2,1,4,5,7,3,5,7,9,3,2,1,4,5,1,1]
    print(delete_duplicated_elements2(array))

#
def delete_duplicated_elements3(array):
    array.sort()
    new_array = []
    for i in range(len(array)):
        if array[i] not in new_array:
            new_array.append(array[i])
    return new_array
if __name__ == '__main__':
    array = [1,2,3,4,2,1,4,5,7,3,5,7,9,3,2,1,4,5,1,1]
    print(delete_duplicated_elements3(array))

#
def delete_duplicated_elements4(array):
    return list(set(array))
if __name__ == '__main__':
    array = [1,2,3,4,2,1,4,5,7,3,5,7,9,3,2,1,4,5,1,1]
    print(delete_duplicated_elements4(array))

#Divide and conquer max and submax
import random as rd
def max_and_submax(seq):
    if len(seq) < 2:
        return seq[0], seq[0]
    if len(seq) == 2:
        if seq[0] > seq[1]:
            return seq[0], seq[1]
        else:
            return seq[1], seq[0]
    x1L, x2L = max_and_submax(seq[:len(seq)//2])
    x1R, x2R = max_and_submax(seq[len(seq)//2:])
    if x1L > x1R:
        if x1R > x2L:
            return x1L, x1R
        else:
            return x1L, x2L
    else:
        if x1L > x2R:
            return x1R, x1L
        else:
            return x1R, x2R
if __name__ == '__main__':
    seq = [rd.randint(0,100) for i in range(20)]
    print(max_and_submax(seq))

#naive fibonacci O(2^n)
def fib1(i):
    assert i >= 0
    if i <= 1:
        return 1
    else:
        return fib1(i-1) + fib1(i-2)
fib1(30)
#memoization 
def fib2(i):
    assert i >= 0
    dic = {}
    if i <= 1:
        dic[i] = 1
        return dic[i]
    elif i in dic:
        return dic[i]
    else:
        dic[i] = fib2(i-1) + fib2(i-2)
        return dic[i]
fib2(30)
#fast fibonacci O(n)
def fib3(n):
    assert n >= 0
    if n <= 1:
        return 1
    pre, next, result = 1, 1, 0
    i = 2
    while(i < n):
        result = pre + next
        pre = next
        next = result
        i += 1
    return result
fib3(100)

def LCS(A, B):
    m, n = len(A), len(B)
    if m == 0 or n == 0:
        return -1
    C = [[0 for i in range(n+1)] for j in range(m+1)]#生成字符串长度加1的0矩阵,C用来保存对应位置匹配的结果
    D = [[None for i in range(n+1)] for j in range(m+1)] #D用来记录转移方向
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                C[i+1][j+1] = C[i][j] + 1
                D[i+1][j+1] = 'equal'
            elif C[i][j+1] > C[i+1][j]:
                C[i+1][j+1] = C[i][j+1]
                D[i+1][j+1] = 'up'
            else:
                C[i+1][j+1] = C[i+1][j]
                D[i+1][j+1] = 'left'
    array = []
    while C[m][n]:
        d = D[m][n]
        if d == 'equal':
            array.append(A[m-1])
            m -= 1
            n -= 1
        elif d == 'up':
            m -= 1
        else:
            n -= 1
    array.reverse()
    return C[-1][-1], array
if __name__ == '__main__':
    A = 'CSPEFC'
    B = 'XCSDYEC'
    print(LCS(A, B))
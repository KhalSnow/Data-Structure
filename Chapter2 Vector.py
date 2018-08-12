# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:49:41 2018

@author: wyh
"""

#binary_search1 O(1.5lgn) 左右转向分支不平衡
def bi_search1(array, object):
    array.sort()
    low, high = 0, len(array)
    while(low < high):
        mid = (low + high) // 2
        if object < array[mid]:
            high = mid
        elif array[mid] < object:
            low = mid + 1
        else:
            return mid
    return -1
if __name__ == '__main__':
    array = [1, 3, 7, 8, 6, 2, 4, 10]
    print("Index: " + str(bi_search1(array, 7)))

#fibonacci_search O(1.44lgn)
#生成fibonacci数列
def fib(n):
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
def fib_search(array, object):
    array.sort()
    low, high = 0, len(array)-1
    k = 0
    while(fib(k)-1 < len(array)):
        k += 1
    while(low < high):
        mid = low + fib(k-1) - 1
        if object < array[mid]:
            high = mid
            k -= 1
        elif array[mid] < object:
            low = mid + 1
            k -= 2
        else:
            return mid
    return -1
if __name__ == '__main__':
    array = [1, 3, 7, 8, 6, 2, 4, 10]
    print("Index: " + str(fib_search(array, 7)))
    print("Index: " + str(fib_search(array, 8)))
    print("Index: " + str(fib_search(array, 2)))
    print("Index: " + str(fib_search(array, 10)))

#binary_search2 左右转向分支平衡
def bi_search2(array, object):
    array.sort()
    low, high = 0, len(array)
    while (1 < high - low):
        mid = (low + high) // 2
        if object < array[mid]:
            high = mid
        else:
            low = mid
    if object == array[low]:
        return low
    else:
        return -1
if __name__ == '__main__':
    array = [1, 3, 7, 8, 6, 2, 4, 10]
    print("Index: " + str(bi_search2(array, 7)))

#binary_search3 实现要求的语义，即返回不大于object的最大值所在的索引
def bi_search3(array, object):
    array.sort()
    low, high = 0, len(array)
    while (low < high):
        mid = (low + high) // 2
        if object < array[mid]:
            high = mid
        else:
            low = mid + 1
    low -= 1
    return low
if __name__ == '__main__':
    array = [1, 3, 7, 8, 6, 2, 4, 10]
    print("Index: " + str(bi_search3(array, 9)))

#interpolation_search O(lglgn)
def in_search(array, object):
    array.sort()
    low, high = 0, len(array)-1
    while(low < high):
        mid = low + int((high - low) * (object - array[low]) / (array[high] - array[low]))
        if object < array[mid]:
            high = mid
        elif array[mid] < object:
            low = mid + 1
        else:
            return mid
    return -1
if __name__ == '__main__':
    array = [1, 3, 7, 8, 6, 2, 4, 10]
    print("Index: " + str(in_search(array, 7)))
    print("Index: " + str(in_search(array, 9)))

#bubble_sort1 O(n^2)
import random as rd
def bubble_sort1(seq):
    for i in range(len(seq)-1):
        for j in range(len(seq)-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq
if __name__ == '__main__':
    seq = [rd.randint(0,100) for i in range(0, 20)]
    print(seq)
    print(bubble_sort1(seq))
    
#bubble_sort2 设置标志，如果有序直接退出
import random as rd
def bubble_sort2(seq):
    sorted = False
    while(not sorted):
        for i in range(len(seq)-1):
            for j in range(len(seq)-i-1):
                if seq[j] > seq[j+1]:
                    seq[j], seq[j+1] = seq[j+1], seq[j]
                    sorted = False
        return seq
if __name__ == '__main__':
    seq = [rd.randint(0,100) for i in range(0, 20)]
    print(seq)
    print(bubble_sort2(seq))

#bubble_sort3 
import random as rd
def bubble_sort3(seq):
    k = len(seq)-1
    for i in range(len(seq)-1):
        mark = 1 #假定每次进入都是有序的，mark为1
        last = 0 #最后一次交换的下标为last
        for j in range(k):
            if seq[j+1] < seq[j]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
                mark = 0 #如果发生交换，则mark置为0
                last = j #保存最后一次交换的下标为j
        if mark == 1:
            break #如果这趟走完，没有发生交换，则原数组有序
        k = last #最后一次交换的位置给k，减少比较的次数
    return seq
if __name__ == '__main__':
    seq = [rd.randint(0,100) for i in range(0, 20)]
    print(seq)
    print(bubble_sort3(seq))

#merge_sort O(nlgn)
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)
def merge(left, right):
    list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list.append(left[i])
            i += 1
        else:
            list.append(right[j])
            j += 1
    list += left[i:]
    list += right[j:]
    return list
if __name__ == '__main__':
    seq = [rd.randint(0,100) for i in range(0, 20)]
    print(seq)
    print(merge_sort(seq))
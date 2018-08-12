# -*- coding: utf-8 -*-
"""
Created on Tue May 22 08:22:22 2018

@author: wyh
"""

#Selection sort O(n^2) Stable
import random as rd
def selection_sort(array):
    if len(array) < 2:
        return array
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                (array[i], array[j]) = (array[j], array[i])
    return(array)
if __name__ == '__main__':
    array = [rd.randint(0,100) for i in range(20)]
    print(array)
    print(selection_sort(array))

#Insertion sort O(n^2) Stable Input sensitive
def insertion_sort(array):
    if len(array) < 2:
        return array
    for i in range(len(array)-1):
        if array[i] < array[i-1]:
            temp = array[i] #当前需要排序的元素
            index = i #用来记录排序元素需要插入的位置
            while (index > 0) and array[index - 1] > temp:
                array[index] = array[index - 1] #已经排序好的元素后移一位，留下需要插入的位置
                index -= 1
            array[index] = temp #把需要排序的元素，插入到指定位置
    return(array)
if __name__ == '__main__':
    array = [rd.randint(0,100) for i in range(20)]
    print(array)
    print(insertion_sort(array))
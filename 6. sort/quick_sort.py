# coding:utf-8
import math

# 基准值为第一位
def quick_sort1(arr):
    if len(arr) <2:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [j for j in arr[1:] if j > pivot]
        return quick_sort1(left) +[pivot] +quick_sort1(right)
def quick_sort2(arr):
    if len(arr) < 2:
        return arr
    else:
        mid_index = math.ceil(len(arr) / 2)
        pivot =  arr.pop(mid_index)
        left = [i for i in arr[0:] if i <= pivot]
        right = [j for j in arr[0:] if j > pivot]
        return quick_sort2(left) + [pivot] + quick_sort2(right)


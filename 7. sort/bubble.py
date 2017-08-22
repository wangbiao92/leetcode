# -*- coding:utf-8 -*-
def bubble_sort(arr):
    for i in range(len(arr) -1 ):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

a = [6,1,5, 5,3,7,13,2]
print(bubble_sort(a))
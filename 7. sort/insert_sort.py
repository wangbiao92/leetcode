# -*- coding:utf-8 -*-
def insert_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        k = i -1
        while k>=0:
            if arr[k] > temp:
                arr[k+1] = arr[k]
                arr[k] = temp
            k -=1
    return arr
print(insert_sort([4,1,2,3,5,2]))
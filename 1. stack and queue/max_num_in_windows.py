# -*- coding:utf-8 -*-

# 对每个滑动窗口内的数进行比较大小，时间复杂度0(n*size)
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0:
            return []
        if size == 1:
            return num
        result = []
        for i in range(0, len(num) - size + 1):
            result.append(max(num[i: i + size]))
        return result


#
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0 or num == [] or len(num) < size:
            return []
        if size == 1:
            return num
        result = []
        index_arr = []
        for i in range(0, len(num)):
            while index_arr and num[i] >= num[index_arr[-1]]:
                index_arr.pop()
            index_arr.append(i)
            if index_arr[0] == i - size:
                index_arr.pop(0)
            if i >= size -1:
                result.append(num[index_arr[0]])
        return result
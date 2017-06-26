# -*- coding:utf-8 -*-
# 斐波那契数列,可以用迭代或者递归（递归容易造成内存溢出）
# 迭代
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0 or number == 1 or number == 2:
            return number
        fx_pre = 1
        fx_cur = 2
        for i in range(number - 2):
            sum = fx_pre + fx_cur
            fx_pre = fx_cur
            fx_cur = sum
        return sum

# 递归
class Solution:
    def jumpFloor(self, number):
        if number == 0 or number == 1 or number == 2:
            return number
        return self.jumpFloor(number-1) + self.jumpFloor(number-2)
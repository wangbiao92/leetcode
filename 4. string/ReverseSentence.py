# -*- coding:utf-8 -*-

# 注意split的使用
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s is None:
            return s
        result = []
        l = s.split(" ")
        for i in range(len(l)-1, -1, -1):
            result.append(l[i])
        return " ".join(result)
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    #测试用例:
    #{8,6,10,5,7,9,11}
    #对应输出应该为:
    #[[8],[6,10],[5,7,9,11]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        res = [] # 结果
        row_node = [pRoot] # 每层的节点
        while len(row_node)>0:
            res.append([])
            # 注意： 无法使用 for i in row_node 遍历二叉树
            for i in range(len(row_node)):
                tmp = row_node.pop(0)
                res[-1].append(tmp.val)
                if tmp.left:
                    row_node.append(tmp.left)
                if tmp.right:
                    row_node.append(tmp.right)
        return res
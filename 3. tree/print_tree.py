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

def max_score(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for k in range(n)]
    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
    return dp[0][n - 1]
def solution(nums):
    if nums is None or len(nums) == 0:
        return 0
    if 0 not in nums:
        return max_score(nums)
    else:
        sum = 0
        arr =[]
        for i in nums:
            if i !=0:
                arr.append(i)
            else:
                sum += max_score(arr)
                arr=[]
        return sum
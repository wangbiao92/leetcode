# -*- coding:utf-8 -*-
# 获得子数组和的最大值

def maxSubArray(nums):
    cur_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        cur_sum = max(nums[i], cur_sum+nums[i])
        max_sum = max(cur_sum, max_sum)
    return max_sum

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
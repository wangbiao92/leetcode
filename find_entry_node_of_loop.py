# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 存在环，找到环的入口， 需要三个指针
class Solution:
    def EntryNodeOfLoop(self, pHead):
        slow1 = slow2 = fast = pHead
        while fast and fast.next:
            fast = fast.next.next
            slow1 = slow1.next
            if fast == slow1:
                while slow1 != slow2:
                    slow1 = slow1.next
                    slow2 = slow2.next
                return slow2

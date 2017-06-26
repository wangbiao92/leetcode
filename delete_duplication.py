# coding:utf-8
# -*- coding:utf-8 -*
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 删除重复的节点，保留一个
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# 删除所有重复的节点，不保留， 如 1→1 返回None
class Solution:
    def deleteDuplication(self, head):
        head_pre = ListNode(-1)
        head_pre.next = head
        pre = head_pre
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.val = cur.next.next.val
                pre.next = cur.next.next
            else:
                pre = cur
                cur = cur.next
        return head_pre.next



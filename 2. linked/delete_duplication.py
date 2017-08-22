# coding:utf-8
# -*- coding:utf-8 -*
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

################
# 注意：删除当前节点需要两个指针
# 删除下一节点 只要一个指针
# 需要删除头节点，必须要在头节点前创造一个节点，用于函数返回这个节点.next

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
        if head is None:
            return None
        head_pre = ListNode(0)
        head_pre.next = head
        pre = head_pre
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                temp = cur.val
                while cur.next and cur.val == temp:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next
        return head_pre.next

# 删除无序链表中的重复元素，保留一个
# 法一：一个指针
def del_duplication(head):
    if not head:
        return None
    element_set = {}
    cur = head
    while cur and cur.next:
        if cur.val in element_set:
            cur.val = cur.next.val
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


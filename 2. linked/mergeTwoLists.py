# -*- coding:utf-8 -*-

# 需要一个节点用来返回，需要一个指针遍历链表
def mergeTwoLists(l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur = l1 or l2
    return dummy.next
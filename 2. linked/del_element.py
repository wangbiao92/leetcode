# -*- coding:utf-8 -*-
# 删除指定元素
# 情况一：不给定节点头（leetcode）

def del_element1(node):
    node.val = node.next.val
    node.next = node.next.next


# 给定节点头以及删除的节点
# 节点头可能为要删除的元素，所以要创建一个节点, 两个指针
def del_elment2(head, num):
    if not head:
        return None
    if not num:
        return head
    head_pre = ListNode(0)
    head_pre.next = head
    pre = head_pre
    cur = head
    while cur:
        if cur.val == num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next

    return head_pre.next


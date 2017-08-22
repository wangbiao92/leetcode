# -*- coding:utf-8 -*-
# 反转单链表
# 需要两个指针
def reverse_single(head):
    pre = None
    cur = head
    while cur:
        next = cur.next  # 3个节点 pre，cur，next
        cur.next = pre  # 反转 指针
        pre = cur  # 移位，遍历链表
        cur = next
    return pre


# 反转双向链表
# 定义两个指针
def reverse_double(head):
    pre = None
    cur = head
    while cur:
        next = cur.next  # 3个节点 pre，cur，next
        cur.next = pre
        cur.prev = next
        pre = cur
        cur = next
    return pre


# 反转部分链表 m 到 n ，分别表示m位，n位 且为整数>=1
# 1、移到需要反转的链表
# 2、按照上面反转的方法，用for来遍历部分节点进行反转
# 注意：考虑到节点头可能被反转，先要创造一个额外的节点

def reverse_part(head, m, n):
    # 特别地， m = n 不反转
    if m == n:
        return head
    head_pre = ListNode(0)
    head_pre.next = head
    pre = head_pre

    # 移位
    for i in range(0, m - 1):
        pre = pre.next

    # 反转链表
    reverse = None
    cur = pre.next
    for i in range(0, n - m + 1):
        next = cur.next
        cur.next = reverse
        reverse = cur
        cur = next
    # 中间部分反转完后， 再拼接再一起
    pre.next.next = cur # 后面一部分
    pre.next = reverse # 反转部分

    return head_pre.next


# 反转前k个节点

def reverse_k_group(head, k):
    if k == 1:
        return head
    head_pre = ListNode(0)
    head_pre.next = head
    pre = head_pre
    cur = head
    for i in range(0, k):
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    head_pre.next.next = cur
    head_pre.next = pre

    return  head_pre
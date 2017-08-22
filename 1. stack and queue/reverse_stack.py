# -*- coding:utf-8 -*-
# 弹出栈底元素，其他元素不变
def get_bottom(stack):
    element = stack.pop()
    if not stack:
        return element #递归停止，返回最后一个元素
    else:
        last = get_bottom(stack)
        stack.append(element)
        return last

def reverse(stack):
    if not stack:
        return
    element = get_bottom(stack)
    reverse(stack)
    stack.append(element)
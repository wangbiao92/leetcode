# -*- coding:utf-8 -*-
# 从上到下递增排序
# 需要额外的栈来保存排序的元素， 再将该栈元素弹出并压入原来的栈中
def sort_stack(stack):
    help_stack = []
    while stack: # 因为stack一直更新，遍历只能用while
        cur = stack.pop()
        while help_stack and cur < help_stack[-1]:
            stack.append(help_stack.pop())
        help_stack.append(cur)
    while help_stack:
        stack.append(help_stack.pop())
    return stack

if __name__ == '__main__':
    stack = [32,91,12,3]
    print(sort_stack(stack))
# -*- coding:utf-8 -*-
# 栈实现队列
# 栈是后进先出，可以用列表表示， 队列是先进先出

class Solution:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
    def push(self, node):
        self.stack_push.append(node)
    def pop(self):
        # 注意：如果self.stack_pop 不为空，再往里面压入数据，根据队列先进先出，应该弹出原来在栈中的，现在弹出刚压入的数据，与队列的属性有违
        if self.stack_pop == []:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()

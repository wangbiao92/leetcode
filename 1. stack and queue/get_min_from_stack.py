# -*- coding:utf-8 -*-
class Solution:
    #
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack:
            self.min_stack.append(node)
        elif node <= self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        # write code here
        if not self.stack:
            return None
        elif self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        # write code here
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def min(self):
        # write code here
        if not self.min_stack:
            return None
        else:
            return self.min_stack[-1]

# -*- coding:utf-8 -*-

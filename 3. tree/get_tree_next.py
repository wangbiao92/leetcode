# -*- coding:utf-8 -*-
class Solution:
    def GetNext(self, pNode):
        # write code here
        # 分3种情况
        # 1） 二叉树为空
        # 2）节点有右子树 → 右子树最左边的那棵树为下一个节点
        # 3）无右子树， a. 为左孩子， 父节点为下一节点， b. 为右孩子
        if pNode is None:
            return None
        if pNode.right:
            tem1 = pNode.right

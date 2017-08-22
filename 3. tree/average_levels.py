# -*- coding:utf-8 -*-
# 输出每一层的均值(遍历数有两个方法，一种是dfs深度优先搜寻（1.前序2.中序3后序）， 另一种是bfs广度优先搜索（分层顺序遍历）)
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# dfs
class Solution1(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levelsum = []
        def dfs(root, depth):
            if root:
                if len(levelsum) <= depth:
                    levelsum.append([0, 0])
                levelsum[depth][0] += root.val
                levelsum[depth][1] += 1
                dfs(root.left, depth+1)
                dfs(root.right, depth+1)
        dfs(root, 0)
        return [sums/float(num) for sums, num in levelsum]

# bfs
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float("inf")
        i = 0
        res = i
        q = [root]
        while q:
            i += 1
            nq = []
            s = 0
            for node in q:
                s += node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q = nq
            if s > max_sum:
                res = i
                max_sum = s
        return res


solution = Solution()
node4 = TreeNode(7)
node5 = TreeNode(-8)
node2 = TreeNode(7, node4, node5)
node3 = TreeNode(0)
root = TreeNode(1, node2, node3)
assert solution.maxLevelSum(root) == 2

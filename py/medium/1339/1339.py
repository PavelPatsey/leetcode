from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = set()

        def _dfs(node: Optional[TreeNode]):
            if node is None:
                return 0
            left = _dfs(node.left)
            right = _dfs(node.right)
            sums.add(left)
            sums.add(right)
            return left + right + node.val

        total = _dfs(root)
        res = max(x * (total - x) for x in sums)
        return res % (10**9 + 7)


solution = Solution()
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
node1 = TreeNode(2, node3, node4)
node2 = TreeNode(3, node5)
node0 = TreeNode(1, node1, node2)
assert solution.maxProduct(node0) == 110

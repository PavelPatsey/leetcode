from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node: Optional[TreeNode], acc: list) -> None:
            if node is None:
                return
            acc = acc + [node.val]
            if node.left is None and node.right is None:
                if sum(acc) == targetSum:
                    res.append(acc)
                return
            dfs(node.left, acc)
            dfs(node.right, acc)

        dfs(root, [])
        return res

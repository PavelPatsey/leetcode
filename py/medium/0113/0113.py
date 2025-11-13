from typing import Optional, List


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
            new_acc = acc + [node.val]
            if node.left is None and node.right is None:
                if sum(new_acc) == targetSum:
                    res.append(new_acc)
                return

            dfs(node.left, new_acc)
            dfs(node.right, new_acc)

        dfs(root, [])
        return res

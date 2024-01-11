from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_node_bfs(self, val):
        if val is None:
            return

        queue = deque([self])
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = TreeNode(val)
                return
            else:
                queue.append(node.left)
            if not node.right:
                node.right = TreeNode(val)
                return
            else:
                queue.append(node.right)

    def print_tree_bfs(self):
        if self is None:
            return
        queue = deque([self])
        while queue:
            node = queue.popleft()
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def print_tree_dfs(self):
        if self:
            print(self.val, end=" ")
            if self.left:
                self.left.print_tree_dfs()
            if self.right:
                self.right.print_tree_dfs()


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)

    def dfs(self, node: Optional[TreeNode], min_value, max_value):
        if not node:
            return 0
        new_min_value = min(node.val, min_value)
        new_max_value = max(node.val, max_value)
        if node.left is None and node.right is None:
            return new_max_value - new_min_value
        return max(
            self.dfs(node.left, new_min_value, new_max_value),
            self.dfs(node.right, new_min_value, new_max_value),
        )


solution = Solution()

root_1 = TreeNode(8)
root_1.left = TreeNode(3)
root_1.left.left = TreeNode(1)
root_1.left.right = TreeNode(6)
root_1.left.right.left = TreeNode(4)
root_1.left.right.right = TreeNode(7)
root_1.right = TreeNode(10)
root_1.right.right = TreeNode(14)
root_1.right.right.left = TreeNode(13)

assert solution.maxAncestorDiff(root_1) == 7

root_2 = TreeNode(1)
root_2.right = TreeNode(2)
root_2.right.right = TreeNode(0)
root_2.right.right.left = TreeNode(3)

assert solution.maxAncestorDiff(root_2) == 3

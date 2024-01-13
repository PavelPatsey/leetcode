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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [node.val]
            return dfs(node.left) + dfs(node.right)

        return dfs(root1) == dfs(root2)


solution = Solution()

root_1 = TreeNode(3)
root_1.left = TreeNode(5)
root_1.left.left = TreeNode(6)
root_1.left.right = TreeNode(2)
root_1.left.right.left = TreeNode(7)
root_1.left.right.right = TreeNode(4)
root_1.right = TreeNode(1)
root_1.right.left = TreeNode(9)
root_1.right.right = TreeNode(8)

root_2 = TreeNode(3)
root_2.left = TreeNode(5)
root_2.left.left = TreeNode(6)
root_2.left.right = TreeNode(7)
root_2.right = TreeNode(1)
root_2.right.left = TreeNode(4)
root_2.right.right = TreeNode(2)
root_2.right.right.left = TreeNode(9)
root_2.right.right.right = TreeNode(8)

root_1.print_tree_bfs()
root_2.print_tree_bfs()

assert solution.leafSimilar(root_1, root_2) is True

root_1 = TreeNode(1)
root_1.left = TreeNode(2)
root_1.right = TreeNode(3)

root_2 = TreeNode(1)
root_2.left = TreeNode(3)
root_2.right = TreeNode(2)

root_1.print_tree_bfs()
root_2.print_tree_bfs()

assert solution.leafSimilar(root_1, root_2) is False

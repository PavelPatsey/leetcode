from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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


class Tree:
    def __init__(self, tree_nodes_data):
        self.tree_nodes = [None] * len(tree_nodes_data)
        for idx, val in enumerate(tree_nodes_data):
            if val:
                self.tree_nodes[idx] = TreeNode(val)
        for idx, _ in enumerate(self.tree_nodes):
            if self.tree_nodes[idx]:
                self.tree_nodes[idx].left = self.left(idx)
                self.tree_nodes[idx].right = self.right(idx)

    def left(self, idx):
        if 2 * idx + 1 < len(self.tree_nodes):
            return self.tree_nodes[2 * idx + 1]
        return None

    def right(self, idx):
        if 2 * idx + 2 < len(self.tree_nodes):
            return self.tree_nodes[2 * idx + 2]
        return None

    def root(self):
        return self.tree_nodes[0]


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

t1 = Tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
t2 = Tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])

assert solution.leafSimilar(t1.root(), t2.root())

t3 = Tree([1, 2, 3])
t4 = Tree([1, 3, 2])

assert not solution.leafSimilar(t3.root(), t4.root())

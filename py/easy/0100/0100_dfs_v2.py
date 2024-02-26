from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    def root(self) -> TreeNode:
        return self.tree_nodes[0]


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node_p: Optional[TreeNode], node_q: Optional[TreeNode]) -> List:
            if not node_p and not node_q:
                return True
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
            return dfs(node_p.left, node_q.left) and dfs(node_p.right, node_q.right)

        return dfs(p, q)


solution = Solution()
null = None

t_1 = Tree([1, 2, 3])
t_2 = Tree([1, 2, 3])
assert solution.isSameTree(t_1.root(), t_2.root()) is True

t_1 = Tree([1, 2])
t_2 = Tree([1, null, 2])
assert solution.isSameTree(t_1.root(), t_2.root()) is False

t_1 = Tree([1, 2, 1])
t_2 = Tree([1, 1, 2])
assert solution.isSameTree(t_1.root(), t_2.root()) is False

from collections import Counter, deque
from typing import Dict, Optional


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

    def root(self) -> TreeNode:
        return self.tree_nodes[0]


class Solution():
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], path_count: Dict):
            if not node:
                return 0

            path_count[node.val] += 1

            if not node.left and not node.right:
                odd_count = sum(count % 2 for count in path_count.values())
                return 1 if odd_count <= 1 else 0
            left_count = dfs(node.left, path_count.copy())
            right_count = dfs(node.right, path_count.copy())
            return left_count + right_count

        initial_path_count = Counter()
        return dfs(root, initial_path_count)


solution = Solution()
null = None

tree = Tree([2, 3, 1, 3, 1, null, 1])
assert solution.pseudoPalindromicPaths(tree.root()) == 2

tree = Tree([2, 1, 1, 1, 3, null, null, null, null, null, 1])
assert solution.pseudoPalindromicPaths(tree.root()) == 1

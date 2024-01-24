from collections import Counter, deque
from functools import reduce
from typing import List, Optional


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


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], path: List):
            if node is None:
                return
            if node.left is None and node.right is None:
                paths.append(path + [node.val])
                return
            dfs(node.left, path + [node.val])
            dfs(node.right, path + [node.val])

        def is_palindrome(lst):
            counter = Counter(lst)
            odds = 0
            for key in counter:
                if counter[key] % 2:
                    odds += 1
                    if odds > 1:
                        break
            else:
                return True
            return False

        paths = []
        dfs(root, [])
        filtered = filter(is_palindrome, paths)
        return reduce(lambda acc, x: acc + 1, filtered, 0)


solution = Solution()
null = None

tree = Tree([2, 3, 1, 3, 1, null, 1])
assert solution.pseudoPalindromicPaths(tree.root()) == 2

tree = Tree([2, 1, 1, 1, 3, null, null, null, null, null, 1])
assert solution.pseudoPalindromicPaths(tree.root()) == 1

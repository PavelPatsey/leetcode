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
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def print_tree_dfs(self):
        if self:
            print(self.val, end=' ')
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

        print(dfs(root1))
        print(dfs(root2))
        return dfs(root1) == dfs(root2)


sulution = Solution()
null = None

lst_1 = [3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]
root_1 = TreeNode(lst_1[0])
for value in lst_1[1:]:
    root_1.insert_node_bfs(value)

lst_2 = [3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8]
root_2 = TreeNode(lst_2[0])
for value in lst_2[1:]:
    root_2.insert_node_bfs(value)

root_1.print_tree_bfs()
root_2.print_tree_bfs()

root_1.print_tree_dfs()
print()
root_2.print_tree_dfs()
print()

assert sulution.leafSimilar(root_1, root_2) is True

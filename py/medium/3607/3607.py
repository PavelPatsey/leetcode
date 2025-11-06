import heapq
from collections import defaultdict, deque


class Solution:
    def processQueries(
        self, c: int, connections: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        traversals = make_traversals(c, graph)
        nodes_info = make_info(c, traversals)
        deleted_nodes = set()
        statuses = [True] * (c + 1)
        res = []
        for command, node in queries:
            if command == 1:
                if statuses[node]:
                    res.append(node)
                else:
                    traversal = traversals[nodes_info[node]]
                    min_node = traversal[0] if traversal else -1
                    res.append(min_node)
            else:
                statuses[node] = False
                deleted_nodes.add(node)
                traversal = traversals[nodes_info[node]]
                while traversal and traversal[0] in deleted_nodes:
                    value = heapq.heappop(traversal)
                    deleted_nodes.remove(value)
        # print(f"{res=}\n")
        return res


def make_traversals(c: int, graph: defaultdict) -> list:
    traversals = []
    visited = set()
    for node in range(1, c + 1):
        if node not in visited:
            traversal = bfs(node, graph)
            visited.update(traversal)
            t = list(traversal)
            heapq.heapify(t)
            traversals.append(t)
    # print(f"{traversals=}")
    return traversals


def bfs(node, matrix) -> set:
    queue = deque([node])
    visited = {node}
    while queue:
        node = queue.popleft()
        children = matrix[node]
        for child in children:
            if child not in visited:
                visited.add(child)
                queue.append(child)
    return visited


def make_info(c: int, traversals: list) -> dict:
    nodes_info = {}
    for node in range(1, c + 1):
        for i, traversal in enumerate(traversals):
            if node in traversal and nodes_info.get(node) is None:
                nodes_info[node] = i
                continue
    # print(f"{nodes_info=}")
    return nodes_info


solution = Solution()
assert solution.processQueries(
    c=5,
    connections=[[1, 2], [2, 3], [3, 4], [4, 5]],
    queries=[[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]],
) == [3, 2, 3]

assert solution.processQueries(
    c=3, connections=[], queries=[[1, 1], [2, 1], [1, 1]]
) == [1, -1]

assert (
    solution.processQueries(
        c=3,
        connections=[[3, 2], [1, 3], [2, 1]],
        queries=[[2, 1]],
    )
    == []
)

assert solution.processQueries(
    c=3,
    connections=[[3, 2], [1, 2]],
    queries=[
        [1, 1],
        [1, 3],
        [2, 2],
        [2, 3],
        [1, 2],
        [2, 1],
        [1, 1],
        [1, 3],
        [1, 2],
        [1, 1],
        [2, 1],
        [1, 1],
        [2, 2],
        [2, 3],
        [2, 1],
        [1, 2],
        [1, 3],
        [2, 1],
        [1, 2],
        [1, 3],
        [2, 1],
        [1, 3],
        [2, 2],
        [1, 1],
        [1, 1],
        [1, 1],
        [2, 1],
        [1, 1],
        [2, 2],
        [1, 3],
        [2, 1],
        [2, 3],
        [2, 2],
        [2, 3],
        [2, 1],
        [1, 1],
        [1, 1],
        [1, 2],
        [2, 2],
        [1, 3],
        [2, 2],
        [1, 3],
        [2, 2],
        [2, 1],
        [2, 1],
        [1, 1],
        [2, 1],
        [1, 1],
        [1, 2],
        [2, 3],
        [2, 1],
        [1, 3],
        [2, 3],
        [2, 1],
        [2, 1],
        [1, 1],
        [1, 1],
        [1, 2],
        [1, 2],
        [1, 1],
        [2, 1],
        [2, 1],
        [2, 3],
        [2, 2],
        [1, 3],
        [1, 2],
        [2, 1],
        [2, 3],
        [2, 2],
        [2, 3],
        [1, 2],
        [1, 3],
        [1, 1],
        [1, 3],
        [2, 2],
        [1, 3],
        [1, 3],
        [1, 2],
        [1, 2],
        [2, 3],
        [1, 3],
        [2, 3],
        [1, 2],
    ],
) == [
    1,
    3,
    1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
]

from collections import defaultdict, deque


class Solution:
    def processQueries(
        self, c: int, connections: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        chains = make_chain(c, connections)
        nodes_info = make_info(c, chains)

        res = []
        for command, node in queries:
            if command == 1:
                if nodes_info[node]["status"]:
                    res.append(node)
                    continue
                chain_id = nodes_info[node]["chain"]
                chain = chains[chain_id]
                min_node = chain[0] if chain else -1
                res.append(min_node)
            else:
                chain_id = nodes_info[node]["chain"]
                chain = chains[chain_id]
                nodes_info[node]["status"] = False
                if node in chain:
                    chain.remove(node)
        print(f"{res=}")
        return res


def make_chain(c: int, connections: list[list[int]]) -> list:
    chains = []
    dependencies = defaultdict(set)
    for u, v in connections:
        dependencies[u].add(v)
    print(f"{dependencies.values()=}")
    children = set()
    for key, value in dependencies.items():
        children.update(value)
    print(f"{children=}")
    for node in range(1, c + 1):
        if node not in children:
            chain = bfs(node, dependencies)
            chains.append(sorted(chain))
    print(f"{chains=}")
    return chains


def make_info(c: int, chains: list) -> dict:
    nodes_info = defaultdict(dict)
    for node in range(1, c + 1):
        nodes_info[node]["status"] = True
        nodes_info[node]["chain"] = None
        for i, chain in enumerate(chains):
            if node in chain:
                nodes_info[node]["chain"] = i
                break

    print(f"{nodes_info=}")
    return nodes_info


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


solution = Solution()
# assert solution.processQueries(
#     c=5,
#     connections=[[1, 2], [2, 3], [3, 4], [4, 5]],
#     queries=[[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]],
# ) == [3, 2, 3]
#
# assert solution.processQueries(
#     c=3, connections=[], queries=[[1, 1], [2, 1], [1, 1]]
# ) == [1, -1]

assert solution.processQueries(
    c=3,
    connections=[[3, 2], [1, 3], [2, 1]],
    queries=[[2, 1]],
) == [1000000]

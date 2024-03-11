class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mapped = map(lambda x: (x, order.find(x)), s)
        _sorted = sorted(mapped, key=lambda x: x[1])
        mapped = map(lambda x: x[0], _sorted)
        return "".join(mapped)


solution = Solution()
assert solution.customSortString("cba", "abcd") == "dcba"

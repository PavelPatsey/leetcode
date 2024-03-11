class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return "".join(sorted(s, key=order.find))


solution = Solution()
assert solution.customSortString("cba", "abcd") == "dcba"

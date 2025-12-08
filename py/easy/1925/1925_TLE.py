from itertools import permutations


class Solution:
    def countTriples(self, n: int) -> int:
        triples = {
            (a, b, c)
            for a, b, c in permutations(range(1, n + 1), 3)
            if a**2 + b**2 == c**2
        }
        return len(triples)


solution = Solution()
assert solution.countTriples(5) == 2
assert solution.countTriples(10) == 4

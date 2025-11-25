class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        res = 1
        n = 1
        while n % k != 0 and res <= k:
            n = n * 10 + 1
            n = n % k
            res += 1
        return res


solution = Solution()
assert solution.smallestRepunitDivByK(1) == 1
assert solution.smallestRepunitDivByK(2) == -1
assert solution.smallestRepunitDivByK(3) == 3
assert solution.smallestRepunitDivByK(6) == -1
assert solution.smallestRepunitDivByK(18367) == 6122

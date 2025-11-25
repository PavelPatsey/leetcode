class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if str(k)[-1] in {"2", "4", "5", "6", "8"}:
            return -1
        n = 1
        b = 1
        rem = b % k
        total = rem
        res = 1
        while total % k != 0 and b % k != 0:
            b = b * 10
            n += b
            rem = b % k
            total = total + rem
            res += 1
        if total % k == 0:
            return res
        return -1


solution = Solution()
assert solution.smallestRepunitDivByK(1) == 1
assert solution.smallestRepunitDivByK(2) == -1
assert solution.smallestRepunitDivByK(3) == 3

class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1

    def _smallestNumber(self, n: int) -> int:
        len_bin_n = len(bin(n)) - 2
        return int(2**len_bin_n - 1)


solution = Solution()
assert solution.smallestNumber(5) == 7
assert solution.smallestNumber(10) == 15
assert solution.smallestNumber(3) == 3

assert solution._smallestNumber(5) == 7
assert solution._smallestNumber(10) == 15
assert solution._smallestNumber(3) == 3

from functools import reduce


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        if len(start_bin) >= len(goal_bin):
            goal_bin = "0" * (len(start_bin) - len(goal_bin)) + goal_bin
        else:
            start_bin = "0" * (len(goal_bin) - len(start_bin)) + start_bin
        filtered = filter(lambda x: x[0] != x[1], zip(start_bin, goal_bin))
        return reduce(lambda acc, x: acc + 1, filtered, 0)


solution = Solution()
assert solution.minBitFlips(10, 7) == 3
assert solution.minBitFlips(3, 4) == 3

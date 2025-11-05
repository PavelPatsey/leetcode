from collections import Counter
from math import prod
from operator import itemgetter


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(xsum(nums[i : i + k], x))
        return res


def xsum(nums: list, x: int) -> int:
    counter = Counter(nums)
    items = list(counter.items())
    sorted_mapped = sorted(items, key=itemgetter(1, 0), reverse=True)
    return sum(prod(n) for n in sorted_mapped[0:x])


solution = Solution()
assert solution.findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2) == [6, 10, 12]
assert solution.findXSum([3, 8, 7, 8, 7, 5], 2, 2) == [11, 15, 15, 15, 12]

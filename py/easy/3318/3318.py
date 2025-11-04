from collections import Counter
from functools import cmp_to_key


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(xsum(nums[i : i + k], x))
        return res


def mycmp(tuple_a, tuple_b) -> int:
    key_a, value_a = tuple_a
    key_b, value_b = tuple_b
    if value_a == value_b:
        if key_a > key_b:
            return 1
        elif key_a < key_b:
            return -1
        else:
            return 0
    if value_a > value_b:
        return 1
    elif value_a < value_b:
        return -1


def xsum(nums: list, x: int) -> int:
    counter = Counter(nums)
    items = list(counter.items())
    sorted_mapped = sorted(items, key=cmp_to_key(mycmp), reverse=True)
    return sum((n[0] * n[1] for n in sorted_mapped[0:x]))


solution = Solution()
assert solution.findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2) == [6, 10, 12]
assert solution.findXSum([3, 8, 7, 8, 7, 5], 2, 2) == [11, 15, 15, 15, 12]

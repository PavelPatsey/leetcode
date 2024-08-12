from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        return sorted(self.nums)[-self.k]


obj = KthLargest(3, [4, 5, 8, 2])
assert obj.add(3) == 4
assert obj.add(5) == 5
assert obj.add(10) == 5
assert obj.add(9) == 8
assert obj.add(4) == 8

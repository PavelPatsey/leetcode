from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for n in nums:
            if n > 0:
                positives.append(n)
            elif n < 0:
                negatives.append(n)
            else:
                assert False
        result = []
        for p, n in zip(positives, negatives):
            result.append(p)
            result.append(n)
        return result


solution = Solution()
assert solution.rearrangeArray([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]

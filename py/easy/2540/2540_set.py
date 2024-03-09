from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_1 = set(nums1)
        set_2 = set(nums2)
        intersection = set_1.intersection(set_2)
        return min(intersection) if intersection else -1


solution = Solution()
assert solution.getCommon([1, 2, 3], [2, 4]) == 2
assert solution.getCommon([1, 2, 3, 6], [2, 3, 4, 5]) == 2
assert solution.getCommon([1], [2]) == -1

nums1 = [11, 15, 28, 31, 36, 42, 46, 54, 58, 63, 64, 67, 75, 76, 76, 79, 83, 85, 87, 90]
nums2 = [3, 6, 8, 13, 15, 19, 22, 25, 29, 29, 32, 35, 43, 43, 48, 55, 81, 90, 91, 94]
assert solution.getCommon(nums1, nums2) == 15

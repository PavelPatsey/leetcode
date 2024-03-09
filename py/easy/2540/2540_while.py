from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        result = -1
        len_i = len(nums1)
        len_j = len(nums2)
        while i < len_i and j < len_j and result == -1:
            while i < len_i and nums1[i] < nums2[j]:
                i += 1
            while i < len_i and j < len_j and nums1[i] > nums2[j]:
                j += 1
            if i < len_i and j < len_j and nums1[i] == nums2[j]:
                result = nums1[i]
        return result


solution = Solution()
assert solution.getCommon([1, 2, 3], [2, 4]) == 2
assert solution.getCommon([1, 2, 3, 6], [2, 3, 4, 5]) == 2
assert solution.getCommon([1], [2]) == -1

nums1 = [11, 15, 28, 31, 36, 42, 46, 54, 58, 63, 64, 67, 75, 76, 76, 79, 83, 85, 87, 90]
nums2 = [3, 6, 8, 13, 15, 19, 22, 25, 29, 29, 32, 35, 43, 43, 48, 55, 81, 90, 91, 94]
assert solution.getCommon(nums1, nums2) == 15

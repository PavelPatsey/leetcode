from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        x = 0
        while x <= len_nums:
            i = 0
            counter = 0
            while i < len_nums:
                if nums[i] >= x:
                    counter += 1
                i += 1
            if counter == x:
                return x
            x += 1
        return -1


solution = Solution()
assert solution.specialArray([3, 5]) == 2
assert solution.specialArray([0, 0]) == -1
assert solution.specialArray([0, 4, 3, 0, 4]) == 3
assert solution.specialArray([3, 6, 7, 7, 0]) == -1

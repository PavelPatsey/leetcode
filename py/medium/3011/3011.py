from typing import List


class Solution:
    @staticmethod
    def _set_bits_number(number: int) -> int:
        return bin(number).count("1")

    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)
        for i in range(N - 1):
            for j in range(N - 1 - i):
                if nums[j] > nums[j + 1]:
                    if self._set_bits_number(nums[j]) == self._set_bits_number(
                        nums[j + 1]
                    ):
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    else:
                        return False
        return True


solution = Solution()
assert solution.canSortArray([8, 4, 2, 30, 15]) is True
assert solution.canSortArray([3, 16, 8, 4, 2]) is False

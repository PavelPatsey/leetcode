from typing import List


class Solution:
    @staticmethod
    def _set_bits_number(number: int) -> int:
        return bin(number).count("1")

    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)
        bit_nums = list(map(lambda x: (x, self._set_bits_number(x)), nums))
        for i in range(N - 1):
            for j in range(N - 1 - i):
                if bit_nums[j][0] > bit_nums[j + 1][0]:
                    if bit_nums[j][1] == bit_nums[j + 1][1]:
                        bit_nums[j], bit_nums[j + 1] = bit_nums[j + 1], bit_nums[j]
                    else:
                        return False
        return True


solution = Solution()
assert solution.canSortArray([8, 4, 2, 30, 15]) is True
assert solution.canSortArray([3, 16, 8, 4, 2]) is False

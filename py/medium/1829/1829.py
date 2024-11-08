from typing import List


class Solution:
    @classmethod
    def get_max_xor(cls, num: int, maximum_bit: int):
        bin_num_str = bin(num)[2:]
        inverted_bin_num = "".join("1" if bit == "0" else "0" for bit in bin_num_str)
        bin_max_xor = "1" * (maximum_bit - len(bin_num_str)) + inverted_bin_num
        max_xor = int(bin_max_xor, 2)
        return max_xor

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_list = [nums[0]]
        prev = nums[0]
        for num in nums[1:]:
            prev = prev ^ num
            xor_list.append(prev)

        return list(map(lambda x: self.get_max_xor(x, maximumBit), xor_list[::-1]))


solution = Solution()
assert solution.get_max_xor(3, 5) == 28
assert solution.get_max_xor(3, 2) == 0
assert solution.get_max_xor(2, 2) == 1



assert solution.getMaximumXor([0, 1, 1, 3], 2) == [0, 3, 2, 3]
assert solution.getMaximumXor([2, 3, 4, 7], 3) == [5, 2, 6, 5]
assert solution.getMaximumXor([0, 1, 2, 2, 5, 7], 3) == [4, 3, 6, 4, 6, 7]

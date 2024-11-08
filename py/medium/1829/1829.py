from typing import List


class Solution:
    @classmethod
    def _get_max_xor(cls, num: int, maximum_bit: int):
        bin_num = bin(num)[2:]
        inverted_bin_num = "".join("1" if bit == "0" else "0" for bit in bin_num)
        bin_max_xor = "1" * (maximum_bit - len(bin_num)) + inverted_bin_num
        max_xor = int(bin_max_xor, 2)
        return max_xor

    @classmethod
    def _get_max_xor_test(cls, num: int, maximum_bit: int):
        max_k = k = 0
        max_xor = num ^ k
        k = 1
        while k < 2**maximum_bit:
            if num ^ k > max_xor:
                max_k = k
                max_xor = num ^ k
            k += 1
        return max_k

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_list = [nums[0]]
        prev = nums[0]
        for num in nums[1:]:
            prev = prev ^ num
            xor_list.append(prev)
        xor_list = xor_list[::-1]

        return


solution = Solution()
assert solution._get_max_xor_test(3, 2) == 0
assert solution._get_max_xor_test(3, 3) == 4
assert solution._get_max_xor_test(0, 2) == 3


assert solution._get_max_xor_test(3, 5) == 28
assert solution._get_max_xor(3, 5) == solution._get_max_xor_test(3, 5)


assert solution._get_max_xor_test(3, 2) == 0
assert solution._get_max_xor(3, 2) == solution._get_max_xor_test(3, 2)

assert solution._get_max_xor_test(2, 2) == 1
assert solution._get_max_xor(3, 2) == solution._get_max_xor_test(3, 2)


# assert solution.getMaximumXor([0, 1, 1, 3], 2) == [0, 3, 2, 3]
# assert solution.getMaximumXor([2, 3, 4, 7], 3) == [5, 2, 6, 5]
# assert solution.getMaximumXor([0, 1, 2, 2, 5, 7], 3) == [4, 3, 6, 4, 6, 7]

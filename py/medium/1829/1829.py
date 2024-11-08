from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_list = [nums[0]]
        prev = nums[0]
        for num in nums[1:]:
            prev = prev ^ num
            xor_list.append(prev)
        xor_list = xor_list[::-1]

        result = []
        for num in xor_list:
            max_k = k = 0
            max_xor = num ^ k
            k = 1
            while k < 2**maximumBit:
                if num ^ k > max_xor:
                    max_k = k
                    max_xor = num ^ k
                k += 1
            result.append(max_k)
        return result


solution = Solution()
assert solution.getMaximumXor([0, 1, 1, 3], 2) == [0, 3, 2, 3]
assert solution.getMaximumXor([2, 3, 4, 7], 3) == [5, 2, 6, 5]
assert solution.getMaximumXor([0, 1, 2, 2, 5, 7], 3) == [4, 3, 6, 4, 6, 7]

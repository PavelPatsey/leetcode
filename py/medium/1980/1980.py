from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        int_nums = sorted(map(lambda x: int(x, 2), nums), reverse=True)
        max_n = 2 ** len(nums) - 1
        n = int_nums.pop()
        i = 0
        result = None
        while i <= max_n and result is None:
            if i < n:
                result = i
            elif int_nums:
                n = int_nums.pop()
            else:
                n = max_n + 1
            i += 1
        if result is not None:
            result = bin(result)[2:].zfill(len(nums))
        return result


solution = Solution()
assert solution.findDifferentBinaryString(["01", "10"]) in {"11", "00"}
assert solution.findDifferentBinaryString(["00", "01"]) in {"11", "10"}
assert solution.findDifferentBinaryString(["111", "011", "001"]) in {
    "000",
    "010",
    "100",
    "110",
    "101",
}

class Solution:
    def findComplement(self, num: int) -> int:
        new_bin_num = ""
        for bit in bin(num)[2:]:
            new_bin_num += "1" if bit == "0" else "0"
        return int(new_bin_num, 2)


solution = Solution()
assert solution.findComplement(5) == 2
assert solution.findComplement(1) == 0

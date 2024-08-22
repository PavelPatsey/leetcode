class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)
        new_bin_num = bin_num[:2]
        for b in bin_num[2:]:
            if b == "1":
                new_bin_num += "0"
            else:
                new_bin_num += "1"
        new_num = int(new_bin_num, 2)
        return new_num


solution = Solution()
assert solution.findComplement(5) == 2
assert solution.findComplement(1) == 0

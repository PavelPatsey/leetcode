class Solution:
    @staticmethod
    def bits_count(num):
        count = 0
        while num:
            count += num & 1
            num = num >> 1
        return count

    def minimizeXor(self, num1: int, num2: int) -> int:
        count_1 = self.bits_count(num1)
        count_2 = self.bits_count(num2)
        if count_1 == count_2:
            return num1
        elif count_1 > count_2:
            bin_x = ""
            for b in bin(num1)[2:]:
                if b == "1" and count_2 > 0:
                    bin_x += "1"
                    count_2 -= 1
                else:
                    bin_x += "0"
            return int(bin_x, 2)
        else:
            bin_x = ""
            count = count_2 - count_1
            for b in reversed(bin(num1)[2:]):
                if b == "0" and count > 0:
                    bin_x += "1"
                    count -= 1
                else:
                    bin_x += b
            bin_x = bin_x[::-1]
            bin_x = "1" * count + bin_x
            return int(bin_x, 2)


solution = Solution()
assert solution.minimizeXor(3, 5) == 3
assert solution.minimizeXor(41, 3) == 40
assert solution.minimizeXor(1, 12) == 3
assert solution.minimizeXor(25, 72) == 24
assert solution.minimizeXor(65, 84) == 67

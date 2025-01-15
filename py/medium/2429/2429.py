class Solution:
    @staticmethod
    def bits_count(num):
        count = 0
        while num:
            count += num & 1
            num = num >> 1
        return count

    def minimizeXor(self, num1: int, num2: int) -> int:
        bits_count = self.bits_count(num2)
        print()
        print(f"{bits_count=}")
        min_tuple = float("inf"), float("inf")
        max_num = (1 << bits_count) - 1
        max_num = max_num << len(bin(num1)[2:])
        max_num += 1
        print(f"{max_num=} {bin(max_num)=}")
        for x in range(max_num):
            if self.bits_count(x) == bits_count:
                y = (min_tuple, (x, x ^ num1))
                min_tuple = min(y, key=lambda x: x[1])
        print(f"{min_tuple=}")
        x = min_tuple[0]
        print(f"{x=}")
        return x


solution = Solution()
assert solution.minimizeXor(3, 5) == 3
assert solution.minimizeXor(1, 12) == 3
assert solution.minimizeXor(25, 72) == 24
assert solution.minimizeXor(3756, 7038) == 3775

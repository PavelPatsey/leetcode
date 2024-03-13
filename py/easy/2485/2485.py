class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) / 2
        current_sum = 0
        i = 1
        result = -1
        while i <= n and result == -1:
            current_sum += i
            if current_sum == total_sum - current_sum + i:
                result = i
            i += 1
        return result


solutions = Solution()
assert solutions.pivotInteger(8) == 6
assert solutions.pivotInteger(1) == 1
assert solutions.pivotInteger(4) == -1

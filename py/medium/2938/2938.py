class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        count = 0
        for char in reversed(s):
            if char == "0":
                count += 1
            elif char == "1":
                result += count
            else:
                assert False, f"invalid character: '{char}'!"
        return result


solution = Solution()
assert solution.minimumSteps("101") == 1
assert solution.minimumSteps("100") == 2
assert solution.minimumSteps("0111") == 0

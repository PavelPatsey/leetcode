from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []

        def dfs(i):
            if i >= len(s):
                result.append(partition.copy())
                return

            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    partition.append(s[i : j + 1])
                    dfs(j + 1)
                    partition.pop()

        dfs(0)
        return result

    @staticmethod
    def is_palindrome(string, left, right):
        while left < right:
            if string[left] != string[right]:
                return False
            left, right = left + 1, right - 1
        return True


solution = Solution()
assert solution.is_palindrome("a", 0, 0) is True
assert solution.is_palindrome("aa", 0, 1) is True
assert solution.is_palindrome("ab", 0, 1) is False

assert solution.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
assert solution.partition("a") == [["a"]]

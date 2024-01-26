class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_i = len(text1)
        len_j = len(text2)
        dp = [[0 for j in range(len_j + 1)] for i in range(len_i + 1)]
        for i in range(len_i - 1, -1, -1):
            for j in range(len_j - 1, -1, -1):
                dp[i][j] = (
                    1 + dp[i + 1][j + 1]
                    if text1[i] == text2[j]
                    else max(dp[i + 1][j], dp[i][j + 1])
                )
        return dp[0][0]


solution = Solution()
assert solution.longestCommonSubsequence("abcde", "ace") == 3
assert solution.longestCommonSubsequence("abc", "abc") == 3
assert solution.longestCommonSubsequence("abc", "def") == 0

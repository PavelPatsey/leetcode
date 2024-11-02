class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.strip().split()
        prev_char = words[-1][-1]
        for word in words:
            if word[0] != prev_char:
                break
            prev_char = word[-1]
        else:
            return True
        return False


solution = Solution()
assert solution.isCircularSentence("lol") is True
assert solution.isCircularSentence("leetcode exercises sound delightful") is True
assert solution.isCircularSentence("eetcode") is True
assert solution.isCircularSentence("Leetcode is cool") is False

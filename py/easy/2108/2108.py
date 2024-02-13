from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


solutions = Solution()
assert solutions.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]) == "ada"
assert solutions.firstPalindrome(["notapalindrome", "racecar"]) == "racecar"
assert solutions.firstPalindrome(["def", "ghi"]) == ""

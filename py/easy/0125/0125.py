class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            if not is_valid(s[l]):
                l += 1
            elif not is_valid(s[r]):
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True


def is_valid(char: str) -> bool:
    return char.isalpha() or char.isdigit()


solution = Solution()
assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
assert solution.isPalindrome("race a car") == False
assert solution.isPalindrome("0P") == False

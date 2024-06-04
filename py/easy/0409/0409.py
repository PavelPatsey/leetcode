class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        result = 0
        for char in s:
            if char in char_set:
                char_set.remove(char)
                result += 2
            else:
                char_set.add(char)
        if char_set:
            result += 1
        return result


solution = Solution()
assert solution.longestPalindrome("abccccdd") == 7
assert solution.longestPalindrome("a") == 1
assert solution.longestPalindrome("asd") == 1
assert solution.longestPalindrome("aassd") == 5
assert solution.longestPalindrome("bb") == 2
s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
assert solution.longestPalindrome(s) == 983

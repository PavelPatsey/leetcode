class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s_list, goal_list = list(s), list(goal)

        for i in range(len(s_list)):
            if s_list == goal_list:
                return True
            new_s_list = [s_list.pop()]
            new_s_list.extend(s_list)
            s_list = new_s_list
        return False


solution = Solution()
assert solution.rotateString("abcde", "cdeab") is True
assert solution.rotateString("abcde", "abced") is False

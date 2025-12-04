class Solution:
    def countCollisions(self, directions: str) -> int:
        stripped_directions = directions.lstrip("L").rstrip("R")
        return len(stripped_directions) - stripped_directions.count("S")


solution = Solution()
assert solution.countCollisions("RLRSLL") == 5
assert solution.countCollisions("LLRR") == 0

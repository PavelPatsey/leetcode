import random


class RandomizedSet:
    def __init__(self):
        self.randomized_set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts an item val into the set if not present.
        Returns true if the item was not present, false otherwise.
        """
        if val in self.randomized_set:
            return False
        self.randomized_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        """
        if val in self.randomized_set:
            self.randomized_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Returns a random element from the current set of elements
        (it's guaranteed that at least one element exists when this method is called).
        Each element must have the same probability of being returned.
        """
        return random.choice(tuple(self.randomized_set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

commands = [
    "RandomizedSet",
    "insert",
    "remove",
    "insert",
    "getRandom",
    "remove",
    "insert",
    "getRandom",
]
input_list = [[], [1], [2], [2], [], [1], [2], []]
output_list = []

obj = RandomizedSet()
output_list.append(None)
output_list.append(obj.insert(1))
output_list.append(obj.remove(2))
output_list.append(obj.insert(2))
output_list.append(obj.getRandom())
output_list.append(obj.remove(1))
output_list.append(obj.insert(2))
output_list.append(obj.getRandom())

print(output_list)
print([None, True, False, True, 2, True, False, 2])

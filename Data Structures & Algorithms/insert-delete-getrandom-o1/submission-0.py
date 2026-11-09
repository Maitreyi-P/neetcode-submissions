class RandomizedSet:

    def __init__(self):
       self.values = []
       self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.values.append(val)
        self.indices[val] = len(self.values) - 1
        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        idx = self.indices[val]
        last_idx = len(self.values) - 1
        last_value = self.values[last_idx]

        self.values[idx] = last_value
        self.values[last_idx] = val
        self.indices[last_value] = idx
        self.values.pop()
        del self.indices[val]
        return True



    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
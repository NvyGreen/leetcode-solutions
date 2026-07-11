class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.vals = []
        

    def insert(self, val: int) -> bool:
        if self.mp.get(val) is not None:
            return False
        
        self.vals.append(val)
        self.mp[val] = len(self.vals) - 1
        
        return True
        

    def remove(self, val: int) -> bool:
        result = self.mp.get(val)
        if result is None:
            return False
        
        rm_index = result
        last_index = len(self.vals) - 1
        
        self.vals[rm_index] = self.vals[last_index]
        self.vals.pop()
        del self.mp[val]
        try:
            self.mp[self.vals[rm_index]] = rm_index
        finally:
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

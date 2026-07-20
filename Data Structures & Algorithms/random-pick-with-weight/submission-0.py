class Solution:

    def __init__(self, w: List[int]):
        self.total_w = sum(w)
        self.w = w

    def pickIndex(self) -> int:
        import random
        w = self.w
        total = self.total_w

        random_number = random.randint(1,total)

        current_weight = 0
        for i,j in enumerate(w):
            current_weight = current_weight + j
            if random_number <= current_weight:
                return i
        
        return len(w)-1

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        pairs = [[key, value] for key, value in count.items()]
        pairs.sort(key=lambda x : x[1], reverse = True)
        return [p[0] for p in pairs[:k]]
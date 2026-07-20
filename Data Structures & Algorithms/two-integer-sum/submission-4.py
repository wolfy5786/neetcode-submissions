class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = dict()
        for i, num in enumerate(nums):
            hp[num] = i
        
        for i, num in enumerate(nums):
            j = (target - num)
            if j in hp and hp[j]!=i:
                return [i, hp[j]]
        
        return []

        
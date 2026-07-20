class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hp = {}
        for num in nums:
            if num in hp:
                return True
            else:
                hp[num] = 1

        return False
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        for indice, num in enumerate(sorted_nums):
            if indice > 0 and sorted_nums[indice-1] == sorted_nums[indice]:
                continue
            left = indice+1
            right = len(sorted_nums)-1
            while left < right:
                if sorted_nums[left] + sorted_nums[right] + num == 0:
                    result.append([sorted_nums[left],sorted_nums[right],num])
                    left = left + 1
                    right = right - 1
                    while sorted_nums[left] == sorted_nums[left-1] and left <right:
                        left = left +1
                elif sorted_nums[left] + sorted_nums[right] + num < 0:
                    left += 1
                else:
                    right -=1 
        return result
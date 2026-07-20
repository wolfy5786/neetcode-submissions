class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i,num in enumerate(nums):
            my_dict[num] = i


        for i,num in enumerate(nums):
            other_pair = target - num
            if other_pair in my_dict:
                if i != my_dict[other_pair]:
                    return [i,my_dict[other_pair]]

        print("not found")
        return [-1,-1]

        
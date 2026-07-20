class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)- 1
        current = min(heights[left], heights[right]) * (right - left)
        while left < right:
            if current < min([heights[left], heights[right]]) * (right -left):
                current = min([heights[left], heights[right]]) * (right - left)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return current



        
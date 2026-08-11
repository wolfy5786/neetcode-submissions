import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        total_left = (n + m + 1) // 2  # elements needed on the left side

        lo, hi = 0, n
        while lo <= hi:
            i = (lo + hi) // 2       # cut point in nums1
            j = total_left - i       # cut point in nums2

            left1  = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i]     if i < n else float('inf')
            left2  = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j]     if j < m else float('inf')

            if left1 <= right2 and left2 <= right1:
                # Correct partition found
                if (n + m) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                hi = i - 1   # i too big, move left
            else:
                lo = i + 1   # i too small, move right

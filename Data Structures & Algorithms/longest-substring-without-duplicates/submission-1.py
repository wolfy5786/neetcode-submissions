class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right  = left + 1
        max_l = right - left
        while right<len(s):
            check = {}
            check[s[left]] = left
            while right<len(s):
                print(s[right])
                if s[right] not in check:
                    check[s[right]] = right
                else:
                    break
                right = right + 1
            print("break")
            s_length = right - left
            print(s_length)
            max_l = max([max_l,s_length])
            if right < len(s):
                left = check[s[right]] + 1
                right = left + 1
            
        return max_l
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = l = 0
        left = right = 0
        track = {}
        while right < len(s):
            track[s[right]] = track.get(s[right],0) + 1
            
            l = right - left + 1
            check = ((l - max(track.values())) <= k)
            if check and l > max_len:
                max_len = l
            elif not check:
                track[s[left]] = track[s[left]] - 1
                left = left + 1 
            right = right + 1

        return max_len




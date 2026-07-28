class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = {}
        len = 0
        max_len = len
        left = 0
        for right, ch in enumerate(s):
            if ch not in track:
                track[ch] = right
                len = len + 1
            else:
                k =track[ch]
                while left<=k:
                    track.pop(s[left])
                    len = len - 1
                    left = left +1
                track[ch] = right
                len = len + 1
            if len > max_len:
                max_len = len

        return max_len

                
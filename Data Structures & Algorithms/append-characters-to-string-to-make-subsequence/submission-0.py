class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        n = len(s)
        m = len(t)
        while j < m:
            if i == n:
                return m - j
            if s[i]==t[j]:
                j = j + 1
            i = i + 1
        return 0
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        if n < m:
            return False
        if m == 0:
            return True

        j = 0 
        for i in range(n):
            if s[j] == t[i]:
                j+=1
            i+=1
            if j == m:
                return True
        return False




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        if len(s)!=len(t):
            return False

        for c in s:
            map[c] = map.get(c,0) + 1
        for c in t:
            if map.get(c,0)-1 < 0:
                return False
            map[c]=map[c]-1

        return True
        

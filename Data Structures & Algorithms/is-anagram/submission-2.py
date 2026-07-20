class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        p = Counter(t)

        return dict(c) == dict(p)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = dict()
        result = []
        index = 0
        for s in strs:
            c = dict(Counter(s))
            c = frozenset(c.items())
            if c in hm:
                l = result[hm[c]]
                l.append(s)
            else:
                hm[c] = index
                index = index + 1
                result.append([s])

        return result



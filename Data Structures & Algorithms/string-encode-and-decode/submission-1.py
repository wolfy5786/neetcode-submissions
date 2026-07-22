class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        result = []
        if s =="":
            return []

        while j< len(s):
            length = 0
            if s[j] == '#':
                length = int(s[i:j])
                result.append(s[j + 1: j + length + 1])
                j = j + length
                i = j + 1
            j = j + 1 
        
        return result

            
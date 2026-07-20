class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check_dict = {}
        for s in s1:
            if s in check_dict:
                check_dict[s] += 1
            else:
                check_dict[s] = 1
        length = len(s1)
        left = 0
        right = 0

        if length == 0:
            return True

        if len(s2)==0:
            return False
        
        while left < len(s2):
            copy = check_dict.copy()

            if s2[left] not in copy:
                left = left +1
                continue

            right = left + length - 1
            

            if right >= len(s2):
                return False
            
            p = left

            while p <= right:
                if s2[p] not in copy:
                    left = p + 1
                    break
                else: 
                    if copy[s2[p]]>0:
                        copy[s2[p]] = copy[s2[p]] - 1
                    else:
                        left = left + 1
                        break
                p += 1

            if p>right:
                return True
        return False 

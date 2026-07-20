import copy

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(t) > len(s)):
            return ""
        

        t_dict = dict()

        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1

        left = 0
        right = 0
        window_size = 100000000000
        left_result = -1
        right_result = -1
        c = copy.deepcopy(t_dict)
        k = list(c.keys())
        print(c)
        right = self.expand_right(left, right, k, s, c)
        print(c)
        left = self.shrink_left(left, right, k, s, c)
        print(c)
        while left <= len(s) - len(t) and right < len(s):
            print(left,right,k,c)
            if len(k)==0:
                left = self.shrink_left(left, right, k, s, c)
                print("selected",left,right)
                ws = right - left + 1
                if ws < window_size and len(k) == 0 :
                    window_size = ws
                    left_result = left
                    right_result = right
            

            if s[left] in c:
                c[s[left]] = c[s[left]] + 1
                if c[s[left]] > 0:
                    k.append(s[left])
            
            left = left + 1
            right = right + 1

            if right < len(s) and s[right] in c:
                c[s[right]] = c[s[right]] - 1
                if c[s[right]] == 0:
                    k.remove(s[right])

        if left_result !=-1:
            return s[left_result:right_result+1]
        else:
            return ""

    def shrink_left(self, left, right, k, s, c):
        while left<right and len(k) == 0 :
            if s[left] in c:
                if c[s[left]] >= 0:
                    break
                c[s[left]] = c[s[left]] + 1
            left = left + 1
        return left

    def expand_right(self,  left, right, k, s, c):
        while right< len(s):
            if s[right] in c:
                c[s[right]] = c[s[right]] - 1
                if c[s[right]] == 0:
                    k.remove(s[right])
            
            if len(k) == 0:
                break

            right = right + 1
        return right




        

        

        
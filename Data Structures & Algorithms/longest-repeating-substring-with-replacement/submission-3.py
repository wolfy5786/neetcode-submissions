class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = left + 1
        max_length = 0

        while right <len(s): 
            length = 1
            first_k = -1
            letter = s[left]
            K= k 
            while right<len(s):
                if letter != s[right]:
                    if first_k == -1:
                        first_k = right
                    K -= 1
                    if K < 0:
                        break

                right += 1
                length += 1

            left = left - 1
            print(left,K,length, right)
            while K>0 and left >=0:
                if letter != s[left]:
                    K -= 1
                length = length +1 
                left = left - 1

            max_length = max([max_length, length])
            if first_k !=-1:
                left = first_k
            else:
                left = right
            right = left + 1
        
        return max_length


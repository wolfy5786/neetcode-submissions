import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i =0 
        s = s.split()
        s = ''.join(s)
        s = s.lower()
        s = re.sub(r'[^a-z0-9]','',s)
        print(s)
        while i<len(s)/2:
            if s[i]!=s[-1*(i+1)]:
                #print(s[i], s[-1*i], s[i+1])
                return False
            i +=1
        return True

        
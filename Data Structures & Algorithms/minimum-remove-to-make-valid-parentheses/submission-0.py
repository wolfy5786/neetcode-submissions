class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_stack = []
        close_stack = []
        if len(s) == 0:
            return s

        for i,ch in enumerate(s):
            if ch =='(':
                open_stack.append(i)
            elif ch ==')':
                if len(open_stack)==0:
                    close_stack.append(i)
                else:
                    open_stack.pop()
        
        remove = set(open_stack+close_stack)
        s = [char for i, char in enumerate(s) if i not in remove]
        return "".join(s)
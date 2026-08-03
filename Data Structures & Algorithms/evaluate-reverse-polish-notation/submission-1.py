class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        result = 0
        for token in tokens:
            try:
                val = int(token)
                nums.append(val)
            except (TypeError, ValueError):
                op = token
                num_1 = nums.pop()
                num_2 = nums.pop()    
                if op == '+':
                    result = num_1 + num_2
                elif op == '-':
                    result = num_2 - num_1
                elif op == '*':
                    result = num_1 * num_2
                else:
                    result = int(num_2 / num_1)
                    
                nums.append(result)

        result = nums.pop()

                    
        
        return result
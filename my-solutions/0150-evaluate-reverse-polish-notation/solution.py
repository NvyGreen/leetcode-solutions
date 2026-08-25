class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            try:
                num = int(token)
                stk.append(num)
            except ValueError:
                num2 = stk.pop()
                num1 = stk.pop()
                result = 0

                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num1 - num2
                elif token == "*":
                    result = num1 * num2
                else:
                    result = int(num1 / num2)
                
                stk.append(result)
        
        return stk[0]

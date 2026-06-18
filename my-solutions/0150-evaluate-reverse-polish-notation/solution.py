class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []

        for token in tokens:
            try:
                values.append(int(token))
            except ValueError:
                val2 = values.pop()
                val1 = values.pop()

                if token == "+":
                    values.append(val1 + val2)
                elif token == "-":
                    values.append(val1 - val2)
                elif token == "*":
                    values.append(val1 * val2)
                else:
                    values.append(int(val1 / val2))
        
        return values[0]
        

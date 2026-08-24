class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stk) > 0 and temperatures[stk[-1]] < temperatures[i]:
                answer[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        
        return answer

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        dec_stk = []

        for i in range(len(temperatures)):
            while len(dec_stk) > 0 and temperatures[dec_stk[-1]] < temperatures[i]:
                old_index = dec_stk.pop()
                answer[old_index] = i - old_index
            dec_stk.append(i)

        return answer

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        combos = []
        for i in range(len(candidates)):
            num = candidates[i]
            combos += self.sumHelper(candidates, target, num, [num], i)
        return combos
    

    def sumHelper(self, candidates: List[int], target: int, runningSum: int, runningList: List[int], index: int) -> List[List[int]]:
        result = []
        if runningSum == target:
            result.append(runningList)
            return result
        elif runningSum > target:
            return result
        
        for i in range(index, len(candidates)):
            num = candidates[i]
            newList = runningList.copy()
            newList.append(num)
            result += self.sumHelper(candidates, target, runningSum + num, newList, i)
        
        return result

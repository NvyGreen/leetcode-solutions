class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        result = []

        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            result += self.helper(candidates, [candidates[i]], candidates[i], target, i)
        
        return result
    

    def helper(self, candidates: List[int], running: List[int], total: int, target: int, index: int) -> List[List[int]]:
        if total == target:
            return [running]
        
        solution = []
        for i in range(index, len(candidates)):
            if total + candidates[i] > target:
                continue
            solution += self.helper(candidates, running + [candidates[i]], total + candidates[i], target, i)
        
        return solution

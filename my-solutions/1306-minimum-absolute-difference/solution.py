class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        minDiff = float('inf')

        for i in range(1, len(arr)):
            currDiff = arr[i] - arr[i - 1]
            if currDiff < minDiff:
                minDiff, result = currDiff, [[arr[i - 1], arr[i]]]
            elif currDiff == minDiff:
                result.append([arr[i - 1], arr[i]])
        
        return result

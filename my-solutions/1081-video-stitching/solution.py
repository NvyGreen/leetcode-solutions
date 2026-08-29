class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        limit, count, i = 0, 0, 0
        longest = [-1, -1]

        while i < len(clips):
            if clips[i][0] > limit:
                if longest == [-1, -1]:
                    return -1
                
                count += 1
                limit = longest[1]
                if limit >= time:
                    return count
                longest = [-1, -1]
                continue
            
            if clips[i][1] >= longest[1]:
                longest = clips[i]
            i += 1
        
        if longest != [-1, -1]:
            count += 1
            limit = longest[1]
        
        return count if limit >= time else -1

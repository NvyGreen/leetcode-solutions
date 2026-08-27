class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        limit, minClips, pointer = 0, 0, 0
        longest = [-1, -1]

        while pointer < len(clips):
            if clips[pointer][0] > limit:
                if longest == [-1, -1]:
                    return -1
                limit = longest[1]
                longest = [-1, -1]
                minClips += 1

                if limit >= time:
                    return minClips
                
                continue
            
            if clips[pointer][1] > longest[1] and clips[pointer][1] > limit:
                longest = clips[pointer]
            
            pointer += 1
        
        if longest != [-1, -1]:
            limit = longest[1]
            minClips += 1
        
        return minClips if limit >= time else -1

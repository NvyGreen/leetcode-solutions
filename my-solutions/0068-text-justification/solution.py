class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified = []
        line = []
        count, length = 0, 0

        for word in words:
            if count == 0 or (maxWidth - (length + len(word))) / count >= 1:
                line.append(word)
                count += 1
                length += len(word)
            else:
                if len(line) == 1:
                    totalSpaces = " " * (maxWidth - len(line[0]))
                    justLine = line[0] + totalSpaces
                else:
                    minSpaces = (maxWidth - length) // (count - 1)
                    spaces = [minSpaces] * (count - 1)

                    charCount = length + minSpaces * (count - 1)
                    i = 0
                    while charCount < maxWidth:
                        spaces[i] += 1
                        charCount += 1
                        i = (i + 1) % len(spaces)
                    
                    justLine = ""
                    for j in range(len(line)):
                        justLine += line[j]
                        if j < len(spaces):
                            justLine += " " * spaces[j]
                
                justified.append(justLine)
                count, length = 1, len(word)
                line = [word]
        
        charCount = length + (count - 1)
        justLine = " ".join(line) + (" " * (maxWidth - charCount))
        justified.append(justLine)

        return justified

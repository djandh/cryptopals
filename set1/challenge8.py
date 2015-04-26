
import challenge4
import itertools

# count number of repeats
def score(s):
    size = 16
    blocks = [s[i:i+size] for i in range(0,len(s),size)]
    pairs = itertools.combinations(blocks, 2)
    return sum([p[0] == p[1] for p in pairs])


if __name__=='__main__':

    lines = challenge4.decodeLines('8.txt')
    
    lineNo, lineCount, maxScore = 0, 0, 0
    for line in lines:
        currScore = score(line)
        if currScore > maxScore:
            maxScore = currScore
            lineNo = lineCount
        lineCount += 1

    print(lineNo)

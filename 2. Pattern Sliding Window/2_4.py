"""def findLongestSubstringWithKDistinctCharacters(kValue, inputArray):
    longestSubstringValue = 0
    windowStart = 0
    windowEnd = 0 
    windowCount = 0
    currentPaceHolder = []
    currentPaceHolderStart = 0
    for windowEnd in range(len(inputArray)):
        if windowEnd < len(inputArray)-1 and inputArray[windowEnd] != inputArray[windowEnd+1]:
            currentPaceHolder.append(inputArray[windowEnd])
        if windowEnd == len(inputArray)-1 and inputArray[windowEnd-1] != inputArray[windowEnd]:
            currentPaceHolder.append(inputArray[windowEnd])
        if len(currentPaceHolder)>kValue and currentPaceHolder.__contains__(inputArray[windowEnd]):
            currentPaceHolder.remove(currentPaceHolder[currentPaceHolderStart])
            currentPaceHolderStart += 1
        elif len(currentPaceHolder)>kValue and not currentPaceHolder.__contains__(inputArray[windowEnd]):
            currentPaceHolder.remove(currentPaceHolder[currentPaceHolderStart])
            currentPaceHolderStart += 1
            longestSubstringValue = max(longestSubstringValue,windowCount)
            while (inputArray[windowStart]) != currentPaceHolder[currentPaceHolderStart]:
                windowCount -= 1
        if currentPaceHolder.__contains__(inputArray[windowEnd]):
            windowCount += 1
    return longestSubstringValue"""


def findLongestSubstringWithKDistinctCharacters(k, inputArray):
    charFreq={}
    start=0
    end=0
    maxSubStringSize=0
    for end in range(len(inputArray)):
        if inputArray[end] not in charFreq:
            charFreq[inputArray[end]]=0
        charFreq[inputArray[end]]+=1
        while len(charFreq)>k:
            charFreq[inputArray[start]]-=1
            if charFreq[inputArray[start]]==0:
                del charFreq[inputArray[start]]
            start+=1
        maxSubStringSize=max(maxSubStringSize,end-start+1)
    return maxSubStringSize

def main():
    result = findLongestSubstringWithKDistinctCharacters(2,"araaci")
    print(result) 
    result = findLongestSubstringWithKDistinctCharacters(3,"cbbebi")
    print(result) 
    
main()

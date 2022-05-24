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
    charFrequency = {}
    windowStart = 0
    windowEnd = 0
    leftChar = 0
    longestSubStringCount = 0
    for windowEnd in range(len(inputArray)):
        currentChar = inputArray[windowEnd]
        if currentChar not in charFrequency:
            charFrequency[currentChar] = 0
        charFrequency[currentChar]+=1
        while len(charFrequency)>k:
            leftChar = inputArray[windowStart]
            charFrequency[leftChar] -=1
            if charFrequency[leftChar]==0:
                del charFrequency[leftChar]
            windowStart += 1
        longestSubStringCount = max(longestSubStringCount,windowEnd-windowStart+1)
    return longestSubStringCount

def main():
    result = findLongestSubstringWithKDistinctCharacters(3,"araaci")
    print(result) 
    result = findLongestSubstringWithKDistinctCharacters(3,"cbbebi")
    print(result) 
    
main()

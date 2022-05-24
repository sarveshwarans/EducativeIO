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
    windowCharFrequency = {}
    longestSubStringLength = 0
    windowStart = 0
    windowEnd = 0
    for windowEnd in range(len(inputArray)):
        currentChar = inputArray[windowEnd]
        if currentChar not in windowCharFrequency:
            windowCharFrequency[currentChar]=0
        windowCharFrequency[currentChar]+=1
        if len(windowCharFrequency)>k:
            leftChar=inputArray[windowStart]
            windowCharFrequency[leftChar]-=1
            if windowCharFrequency[leftChar]==0:
                del windowCharFrequency[leftChar]
            windowStart+=1
        currentWindowLength = windowEnd-windowStart+1
        longestSubStringLength = max(longestSubStringLength,currentWindowLength) 
    return longestSubStringLength


def main():
    result = findLongestSubstringWithKDistinctCharacters(3,"araaci")
    print(result) 
    result = findLongestSubstringWithKDistinctCharacters(3,"cbbebi")
    print(result) 
    
main()

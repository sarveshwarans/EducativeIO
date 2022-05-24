def findLongestSubStringWithSameLettersAfterReplacement(kValue,inputArray):
    windowStart = 0
    windowEnd = 0
    maxRepeatCharCount = 0
    longSubStringCount = 0
    windowFreq ={}
    for windowEnd in range(len(inputArray)):
        currentChar = inputArray[windowEnd]
        if currentChar not in windowFreq:
            windowFreq[currentChar]=0
        windowFreq[currentChar]+=1
        maxRepeatCharCount = max(maxRepeatCharCount,windowFreq[currentChar])
        currentWindowSize = windowEnd-windowStart+1
        if currentWindowSize-maxRepeatCharCount>kValue:
            leftChar=inputArray[windowStart]
            windowFreq[leftChar]-=1
            if windowFreq[leftChar]==0:
                del windowFreq[leftChar]
            windowStart+=1
        longSubStringCount = max(longSubStringCount,windowEnd-windowStart+1)    
    return longSubStringCount


def main():
    print(findLongestSubStringWithSameLettersAfterReplacement(2,"aabccbb"))
    print(findLongestSubStringWithSameLettersAfterReplacement(1,"abbcb"))
    print(findLongestSubStringWithSameLettersAfterReplacement(1,"abccde"))
    
main()
        
"""Logic: CurrentProcessingWindowSize - MaxRepeatCharacterCount > K, then the window is invalid"""
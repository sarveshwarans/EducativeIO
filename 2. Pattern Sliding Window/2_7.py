def findLongestSubStringWithSameLettersAfterReplacement1(kValue,inputArray):
    charFrequency = {}
    windowStart = 0
    windowEnd = 0
    maxSubStringCount = 0 
    maxRepeatCharacterCount = 0
    for windowEnd in range(len(inputArray)):
        currentChar = inputArray[windowEnd]
        if currentChar not in charFrequency:
            charFrequency[currentChar] = 0
        charFrequency[currentChar]+=1
        maxRepeatCharacterCount = max(maxRepeatCharacterCount,charFrequency[currentChar])
        if windowEnd-windowStart+1 - maxRepeatCharacterCount > kValue:
            leftChar = inputArray[windowStart]
            charFrequency[leftChar] -=1
            if charFrequency[leftChar]==0:
                del charFrequency[leftChar]
            windowStart+=1
        maxSubStringCount = max(maxSubStringCount,windowEnd-windowStart+1)
    return maxSubStringCount


def findLongestSubStringWithSameLettersAfterReplacement(kValue,inputArray):
    start=0
    longestSubStringDistance=0
    windowFreq={}
    maxFreqInWindow=0
    for end in range(len(inputArray)):
        currentChar=inputArray[end]
        if currentChar not in windowFreq:
            windowFreq[currentChar]=0
        windowFreq[currentChar]+=1
        maxFreqInWindow=max(maxFreqInWindow,windowFreq[currentChar])
        currentWindowLength=end-start+1
        if currentWindowLength-maxFreqInWindow>kValue:
            leftMostChar=inputArray[end]
            windowFreq[leftMostChar]-=1
            if windowFreq[leftMostChar]==0:
                del windowFreq[leftMostChar]
            start+=1
        longestSubStringDistance=max(longestSubStringDistance,currentWindowLength)   
    return longestSubStringDistance 

def main():
    print(findLongestSubStringWithSameLettersAfterReplacement(2,"aabccbb"))
    print(findLongestSubStringWithSameLettersAfterReplacement(1,"abbcb"))
    print(findLongestSubStringWithSameLettersAfterReplacement(1,"abccde"))
    
main()
        
"""Logic: CurrentProcessingWindowSize - MaxRepeatCharacterCount > K, then the window is invalid"""
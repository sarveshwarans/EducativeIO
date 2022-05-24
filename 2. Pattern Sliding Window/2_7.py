def findLongestSubStringWithSameLettersAfterReplacement(kValue,inputArray):
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

def main():
    print(findLongestSubStringWithSameLettersAfterReplacement(2,"aabccbb"))
    print(findLongestSubStringWithSameLettersAfterReplacement(1,"abbcb"))
    print(findLongestSubStringWithSameLettersAfterReplacement(1,"abccde"))
    
main()
        
"""Logic: CurrentProcessingWindowSize - MaxRepeatCharacterCount > K, then the window is invalid"""
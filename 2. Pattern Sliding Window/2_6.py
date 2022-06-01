def findNoRepeatSubString1(inputArray):
    windowStart = 0
    windowEnd = 0 
    maxSubStringCount = 0
    for windowEnd in range(len(inputArray)-1):
        currentChar = inputArray[windowEnd]
        nextChar = inputArray[windowEnd+1]
        if currentChar == nextChar:
            windowStart = windowEnd+1
        else:
            maxSubStringCount = max(maxSubStringCount, windowEnd-windowStart+2)
    return maxSubStringCount


def findNoRepeatSubString2(inputArray):
    windowStart = 0 
    windowEnd = 0
    charFrequence = {}
    maxSubStringCount = 0
    for windowEnd in range(len(inputArray)):
        currentChar = inputArray[windowEnd]
        if currentChar not in charFrequence:
            charFrequence[currentChar] = 0
            maxSubStringCount = max(maxSubStringCount,windowEnd-windowStart+1)
            charFrequence[currentChar] += 1
        else:
            charFrequence[currentChar] += 1
            while charFrequence[currentChar] == 1:
                leftChar = inputArray[windowStart]
                charFrequence[leftChar] -= 1
                if charFrequence[leftChar] == 0:
                    del charFrequence[leftChar]
                windowStart += 1
            windowStart = windowEnd
    return maxSubStringCount

def findNoRepeatSubString(inputArray):
    start=0
    windowFreq={}
    stringLength=0
    for end in range(len(inputArray)):
        currentChar=inputArray[end]
        if currentChar not in windowFreq:
            windowFreq[currentChar]=0
        windowFreq[currentChar]+=1
        if windowFreq[currentChar]==1:
            stringLength=max(stringLength,end-start+1)
        else:
            windowFreq={}
            windowFreq[currentChar]=1
            start=end
    return stringLength


def main():
    print(findNoRepeatSubString("abbbb"))
    print(findNoRepeatSubString("aabccbb"))
    print(findNoRepeatSubString("abccde"))
    
main()

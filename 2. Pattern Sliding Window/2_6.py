from re import sub


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


def findNoRepeatSubString(inputArray):
    windowStart = 0
    windowEnd = 0
    windowFreq = {}
    subStringLength = 0
    for windowEnd in range(len(inputArray)):
        currentChar = inputArray[windowEnd]
        if currentChar not in windowFreq:
            windowFreq[currentChar]=1
            subStringLength = max(subStringLength,windowEnd-windowStart+1)
        else:
            windowStart=windowEnd
            windowFreq={}
    return subStringLength




def main():
    print(findNoRepeatSubString("abbbb"))
    print(findNoRepeatSubString("aabccbb"))
    print(findNoRepeatSubString("abccde"))
    
main()

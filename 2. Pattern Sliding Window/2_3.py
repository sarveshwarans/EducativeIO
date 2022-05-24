import sys
"""def smallestSubarrayWithAGivenSum(sumK, inputArray):
    smallestArraySizeOutput = sys.maxsize
    windowStart = 0
    windowStop = 0
    windowSum = 0
    windowSize = 0
    for windowStop in range(len(inputArray)):
        windowSum += inputArray[windowStop]
        windowSize += 1
        if windowSum >= sumK:
            smallestArraySizeOutput = min(smallestArraySizeOutput, windowSize)
            windowSum -= inputArray[windowStart]
            windowStart += 1
            windowSize -= 1
            while(windowSum>=sumK):
                windowSize -= 1
                smallestArraySizeOutput = min(smallestArraySizeOutput, windowSize)
                windowSum -= inputArray[windowStart]
                windowStart += 1
    return smallestArraySizeOutput
"""

def smallestSubarrayWithAGivenSum(sizeK, inputArray):
    windowStart = 0
    windowEnd = 0 
    smallestSubArraySize = sys.maxsize
    windowSize = 0
    windowSum = 0
    for windowEnd in range(len(inputArray)):
        windowSum += inputArray[windowEnd]
        windowSize += 1
        while windowSum >= sizeK:
            smallestSubArraySize = min (smallestSubArraySize, windowSize)
            windowSum -= inputArray[windowStart]
            windowStart += 1
            windowSize -= 1
    return smallestSubArraySize

def main():
    result = smallestSubarrayWithAGivenSum(8,[3, 4, 1, 1, 6])
    print(result) 
    
main()



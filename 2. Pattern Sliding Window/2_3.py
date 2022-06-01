import sys

from pkg_resources import require
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

def smallestSubarrayWithAGivenSum1(givenSum, inputArray):
    start=0
    end=0
    windowSum=0
    requiredSize=sys.maxsize
    for end in range(len(inputArray)):
        windowSum+=inputArray[end]
        while windowSum>=givenSum:
            requiredSize=min(requiredSize,end-start+1)
            windowSum-=inputArray[start]
            start+=1
    return requiredSize



def main():
    result = smallestSubarrayWithAGivenSum1(4,[3, 4, 1, 1, 6])
    print(result) 
    
main()



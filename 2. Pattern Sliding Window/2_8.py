def findLongestSubarryWithOnesAfterReplacement1(kSize,inputArray):
    windowStart = 0
    windowEnd = 0
    numberFrequence = {}
    maxLongestSubArrayCount = 0 
    maxFrequenceOfOne = 0
    for windowEnd in range(len(inputArray)):
        currentNumber = inputArray[windowEnd]
        if currentNumber not in numberFrequence:
            numberFrequence[currentNumber] = 0
        numberFrequence[currentNumber] += 1
        if currentNumber == 1:
            maxFrequenceOfOne = numberFrequence[currentNumber]
        if windowEnd-windowStart+1 - maxFrequenceOfOne > kSize:
            leftNumber = inputArray[windowStart]
            numberFrequence[leftNumber] -= 1
            if numberFrequence[leftNumber] == 0:
                del numberFrequence[leftNumber]
            windowStart += 1
        maxLongestSubArrayCount = max(maxLongestSubArrayCount, windowEnd-windowStart+1)
    return maxLongestSubArrayCount


def findLongestSubarryWithOnesAfterReplacement(kSize,inputArray):
    start=0
    onesLengthAfterReplacement=0
    numberFreq={}
    for end in range(len(inputArray)):
        currentNumber=inputArray[end]
        if currentNumber not in numberFreq:
            numberFreq[currentNumber]=0
        numberFreq[currentNumber]+=1
        if numberFreq[0]>kSize:
            leftMostNumber=inputArray[start]
            numberFreq[leftMostNumber]-=1
            if numberFreq[leftMostNumber]==0:
                del numberFreq[leftMostNumber]
            start+=1
        currentLength=end-start+1
        onesLengthAfterReplacement=max(onesLengthAfterReplacement,currentLength)
    return onesLengthAfterReplacement


def main():
    print(findLongestSubarryWithOnesAfterReplacement(2,[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]))
    print(findLongestSubarryWithOnesAfterReplacement(3,[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]))
    
main()
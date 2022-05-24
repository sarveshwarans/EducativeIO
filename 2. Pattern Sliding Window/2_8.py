def findLongestSubarryWithOnesAfterReplacement(kSize,inputArray):
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

def main():
    print(findLongestSubarryWithOnesAfterReplacement(2,[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]))
    print(findLongestSubarryWithOnesAfterReplacement(3,[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]))
    
main()
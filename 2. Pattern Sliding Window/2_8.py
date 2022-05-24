def findLongestSubarryWithOnesAfterReplacement(kSize,inputArray):
    numFreq ={}
    windowStart=0
    windowEnd=0
    longestSubArray = 0
    for windowEnd in range(len(inputArray)):
        currentNum = inputArray[windowEnd]
        if currentNum not in numFreq:
            numFreq[currentNum]=0
        numFreq[currentNum]+=1
        while numFreq[0]>kSize:
            leftNumber = inputArray[windowStart]
            numFreq[leftNumber]-=1
            if numFreq[leftNumber]==0:
                del numFreq[leftNumber]
            windowStart+=1
        longestSubArray = max(longestSubArray,windowEnd-windowStart+1)
    return longestSubArray

def main():
    print(findLongestSubarryWithOnesAfterReplacement(2,[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]))
    print(findLongestSubarryWithOnesAfterReplacement(3,[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]))
    
main()
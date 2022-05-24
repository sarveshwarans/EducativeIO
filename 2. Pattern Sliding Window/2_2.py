def findMaximumSumSubArrayOfSizeK(sizeK, inputArray):
    maxValueOutput = 0
    windowStart = 0 
    windowEnd = 0
    windowSum = 0
    for windowEnd in range(len(inputArray)):
        windowSum += inputArray[windowEnd]
        if windowEnd >= sizeK-1 :
            maxValueOutput = max(maxValueOutput,windowSum)
            windowSum -= inputArray[windowStart]
            windowStart += 1
    return maxValueOutput

def main():
    result = findMaximumSumSubArrayOfSizeK(3,[2,1,5,1,3,2])
    print(result) 
    
main()
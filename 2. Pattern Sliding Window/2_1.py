def findAverageOfKInInputArray(sizeK,inputArray):
    windowStart = 0
    windowEnd = 0
    windowSum = 0
    outputList = []
    for windowEnd in range(len(inputArray)):
        windowSum += inputArray[windowEnd]
        if windowEnd>=sizeK-1:
            outputList.append(windowSum/sizeK)
            windowSum-=inputArray[windowStart]
            windowStart+=1
    return outputList


def main():
    result = findAverageOfKInInputArray(5,[1,3,2,6,-1,4,1,8,2])
    print(result) 
    
main()
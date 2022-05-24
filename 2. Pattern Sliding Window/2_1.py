def findAverageOfKInInputArray(sizeK,inputArray):
    outputArray = []
    windowStart = 0
    windowEnd = 0
    windowSum = 0 
    for windowEnd in range(len(inputArray)):
        windowSum += inputArray[windowEnd]
        if windowEnd >= sizeK - 1:
            outputArray.append(windowSum/sizeK)
            windowSum -= inputArray[windowStart]
            windowStart += 1
    return outputArray

def main():
    result = findAverageOfKInInputArray(5,[1,3,2,6,-1,4,1,8,2])
    print(result) 
    
main()
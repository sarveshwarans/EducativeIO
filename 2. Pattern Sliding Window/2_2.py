def findMaximumSumSubArrayOfSizeK(sizeK, inputArray):
    maxSum=0
    start=0
    end=0
    windowSum=0
    for end in range(len(inputArray)):
        windowSum+=inputArray[end]
        if end>=sizeK-1:
            maxSum=max(maxSum,windowSum)
            windowSum-=inputArray[start]
            start+=1
    return maxSum

def main():
    result = findMaximumSumSubArrayOfSizeK(3,[2,1,5,1,3,2])
    print(result) 
    
main()
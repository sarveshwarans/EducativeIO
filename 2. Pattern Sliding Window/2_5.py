def findFruitsIntoBasket(inputArray):
    windowStart = 0
    windowEnd = 0
    maxFruitCount = 0
    windowFruitFreq = {}
    for windowEnd in range(len(inputArray)):
        currentFruit = inputArray[windowEnd]
        if currentFruit not in windowFruitFreq:
            windowFruitFreq[currentFruit]=0
        windowFruitFreq[currentFruit]+=1
        while len(windowFruitFreq)>2:
            leftFruit=inputArray[windowStart]
            windowFruitFreq[leftFruit]-=1
            if windowFruitFreq[leftFruit]==0:
                del windowFruitFreq[leftFruit]
            windowStart+=1
        maxFruitCount = max(maxFruitCount,windowEnd-windowStart+1)
    return maxFruitCount

def main():
    result = findFruitsIntoBasket(['A', 'B', 'C', 'B', 'B', 'C'])
    print(result) 
    print(findFruitsIntoBasket(['A', 'B', 'C', 'A', 'C']))
    
main()

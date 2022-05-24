def findFruitsIntoBasket(inputArray):
    currentFruit = 0
    windowStart = 0
    windowEnd = 0
    maxFruitCount = 0 
    fruitFrequence = {}
    for windowEnd in range(len(inputArray)):
        currentFruit = inputArray[windowEnd]
        if currentFruit not in fruitFrequence:
            fruitFrequence[currentFruit] = 0
        fruitFrequence[currentFruit] += 1
        while len(fruitFrequence)>2:
            leftFruit = inputArray[windowStart]
            fruitFrequence[leftFruit] -= 1
            if fruitFrequence[leftFruit] == 0:
                del fruitFrequence[leftFruit]
            windowStart += 1
        maxFruitCount = max(maxFruitCount, windowEnd-windowStart+1)
    return maxFruitCount

def main():
    result = findFruitsIntoBasket(['A', 'B', 'C', 'B', 'B', 'C'])
    print(result) 
    print(findFruitsIntoBasket(['A', 'B', 'C', 'A', 'C']))
    
main()

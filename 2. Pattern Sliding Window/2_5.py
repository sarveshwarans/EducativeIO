from turtle import st


def findFruitsIntoBasket(inputArray):
    fruitFreq={}
    maxCount=0
    start=0
    for end in range(len(inputArray)):
        currentFruit=inputArray[end]
        if currentFruit not in fruitFreq:
            fruitFreq[currentFruit]=0
        fruitFreq[currentFruit]+=1
        while len(fruitFreq)>2:
            leftMostFruit=inputArray[start]
            fruitFreq[leftMostFruit]-=1
            if fruitFreq[leftMostFruit]==0:
                del fruitFreq[leftMostFruit]
            start+=1
        maxCount=max(maxCount,end-start+1)
    return maxCount

def main():
    result = findFruitsIntoBasket(['A', 'B', 'C', 'B', 'B', 'C'])
    print(result) 
    print(findFruitsIntoBasket(['A', 'B', 'C', 'A', 'C']))
    
main()

from collections import deque

def squareOfNumbersInSortedOrder1(inputList):
    lP,rP=0,len(inputList)-1
    highestIndex=len(inputList)-1
    outputList=[0 for x in range(len(inputList))]
    while lP<rP:
        leftSquare=inputList[lP]*inputList[lP]
        rightSquare=inputList[rP]*inputList[rP]
        if leftSquare<rightSquare:
            outputList[highestIndex]=rightSquare
            highestIndex-=1
            rP-=1
        else:
            outputList[highestIndex]=leftSquare
            highestIndex-=1
            lP+=1
    return outputList

def squareOfNumbersInSortedOrder(inputList):
    outputList=deque()
    l,r=0,len(inputList)-1
    while l<=r:
        if abs(inputList[l])>abs(inputList[r]):
            outputList.appendleft(inputList[l]*inputList[l])
            l+=1
        elif abs(inputList[l])<=abs(inputList[r]):
            outputList.appendleft(inputList[r]*inputList[r])
            r-=1
    return list(outputList)


def main():
    print(squareOfNumbersInSortedOrder([-2, -1, 0, 2, 3]))
    print(squareOfNumbersInSortedOrder([-3, -1, 0, 1, 2]))  
main()
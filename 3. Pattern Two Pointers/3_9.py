def quadrapleSumToTarget(target,inpList):
    inpList.sort()
    outerLeft=0
    outList=[]
    for currentIndex in range(len(inpList)-3):
        if currentIndex>0 and inpList[currentIndex]==inpList[currentIndex-1]:
            continue
        firstElementInQuad = inpList[currentIndex]
        targerForFirstElement = target-firstElementInQuad
        firstLeft=currentIndex+1
        firstRight=len(inpList)-1
        if firstLeft>currentIndex+1 and inpList[firstLeft]==inpList[firstLeft-1]:
            continue
        while firstLeft<firstRight:
            firstLeftNumber=inpList[firstLeft]
            twoSumTarget=targerForFirstElement-firstLeftNumber
            secondLeft=firstLeft+1
            secondRight=len(inpList)-1
            while secondLeft<secondRight:
                secondLeftNumber=inpList[secondLeft]
                rightNumber=inpList[secondRight]
                currentSum=secondLeftNumber+rightNumber
                if currentSum==twoSumTarget:
                    outList.append([firstElementInQuad,firstLeftNumber,inpList[secondLeft],inpList[secondRight]])
                    secondLeft+=1
                    secondRight-=1
                    while secondLeft<secondRight and inpList[secondLeft]==inpList[secondLeft-1]:
                        secondLeft+=1
                    while secondLeft<secondRight and inpList[secondRight]==inpList[secondRight+1]:
                        secondRight-=1
                elif currentSum<twoSumTarget:
                    secondLeft+=1
                else:
                    secondRight-=1
            firstLeft+=1
    return outList

def quadrapleSumToTargetNew(target,inpList):
    inpList.sort()
    outList=[]
    for firstNumberIndex in range(len(inpList)):
        if firstNumberIndex>0 and inpList[firstNumberIndex]==inpList[firstNumberIndex-1]:
            continue
        for secondNumberIndex in range(firstNumberIndex+1,len(inpList)):
            if secondNumberIndex>firstNumberIndex+1 and inpList[secondNumberIndex]==inpList[secondNumberIndex-1]:
                continue                
            firstNumber = inpList[firstNumberIndex]
            secondNumber = inpList[secondNumberIndex]
            thirdNumberIndex=secondNumberIndex+1
            fourthNumberIndex=len(inpList)-1
            while thirdNumberIndex<fourthNumberIndex:
                thirdNumber=inpList[thirdNumberIndex]
                fourthNumber=inpList[fourthNumberIndex]
                currentSum=firstNumber+secondNumber+thirdNumber+fourthNumber
                if currentSum==target:
                    outList.append([firstNumber,secondNumber,thirdNumber,fourthNumber])
                    thirdNumberIndex+=1
                    fourthNumberIndex-=1
                    while thirdNumberIndex<fourthNumberIndex and inpList[thirdNumberIndex]==inpList[thirdNumberIndex-1]:
                        thirdNumberIndex+=1
                    while thirdNumberIndex<fourthNumberIndex and inpList[fourthNumberIndex]==inpList[fourthNumberIndex+1]:
                        fourthNumberIndex-=1
                elif currentSum<target:
                    thirdNumberIndex+=1
                else:
                    fourthNumberIndex-=1
    return outList


def main():
    print(quadrapleSumToTarget(1,[4, 1, 2, -1, 1, -3])) 
    print(quadrapleSumToTarget(2,[2, 0, -1, 1, -2, 2]))
    print(quadrapleSumToTarget(8,[2,2,2,2,2]))
    print(quadrapleSumToTargetNew(1,[4, 1, 2, -1, 1, -3])) 
    print(quadrapleSumToTargetNew(2,[2, 0, -1, 1, -2, 2]))
    print(quadrapleSumToTargetNew(8,[2,2,2,2,2]))

main()
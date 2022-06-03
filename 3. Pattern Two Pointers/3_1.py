from turtle import left


def pairWithTargetSum1(target,inputList):
    leftPointer,rightPointer=0,len(inputList)-1
    outputIndices=[]
    while leftPointer<rightPointer:
        currentSum = inputList[leftPointer]+inputList[rightPointer]
        if currentSum==target:
            outputIndices = [leftPointer,rightPointer]
            return outputIndices
        elif currentSum<target:
            leftPointer+=1
        elif currentSum>target:
            rightPointer-=1

def pairWithTargetSumUsingHM1(target,inputList):
    hashMap ={}
    for currentIndex,currentNumber in enumerate(inputList):
        requiredNumber = target-currentNumber
        if requiredNumber not in hashMap:
            hashMap[currentNumber]=currentIndex
        else:
            return [currentIndex,hashMap[requiredNumber]]
        

def pairWithTargetSum(target,inputList):
    l=0
    r=len(inputList)-1
    while l<r:
        currentSum=inputList[l]+inputList[r]
        if currentSum==target:
            #return[inputList[l],inputList[r]]
            return[l,r]
        elif currentSum<target:
            l+=1
        else:
            r-=1
    return []

def pairWithTargetSumUsingHM(target,inputList):
    hashMap={}
    for index,number in enumerate(inputList):
        iAmLookingFor=target-number
        if iAmLookingFor not in hashMap:
            hashMap[number]=index
        else:
            #return [number,inputList[hashMap[iAmLookingFor]]]
            return[index,hashMap[iAmLookingFor]]
    return []


def main():
    print(pairWithTargetSum(6,[1, 2, 3, 4, 6]))
    print(pairWithTargetSum(11,[2, 5, 9, 11]))  
    print(pairWithTargetSumUsingHM(6,[1, 2, 3, 4, 6]))
    print(pairWithTargetSumUsingHM(11,[2, 5, 9, 11]))  

main()





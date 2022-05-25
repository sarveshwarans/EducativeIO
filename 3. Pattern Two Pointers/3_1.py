from turtle import left


def pairWithTargetSum(target,inputList):
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

def pairWithTargetSumUsingHM(target,inputList):
    hashMap ={}
    for currentIndex,currentNumber in enumerate(inputList):
        requiredNumber = target-currentNumber
        if requiredNumber not in hashMap:
            hashMap[currentNumber]=currentIndex
        else:
            return [currentIndex,hashMap[requiredNumber]]
        

def main():
    print(pairWithTargetSum(6,[1, 2, 3, 4, 6]))
    print(pairWithTargetSum(11,[2, 5, 9, 11]))  
    print(pairWithTargetSumUsingHM(6,[1, 2, 3, 4, 6]))
    print(pairWithTargetSumUsingHM(11,[2, 5, 9, 11]))  

main()





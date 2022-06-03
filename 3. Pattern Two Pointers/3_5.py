import sys
def tripletSumCloseToTarget1(target,inputList):
    inputList.sort()
    lP,rP=0,len(inputList)-1
    howClose=sys.maxsize
    tripletOutputSum=0
    for i in range(len(inputList)-1):
        lP=i+1
        rP=len(inputList)-1
        while lP<rP:
            currentSum=inputList[lP]+inputList[rP]+inputList[i]
            if currentSum>target:
                rP-=1
            elif currentSum<target:
                lP+=1
            else:
                return currentSum
            # Target=5 and Current=4 -> 5-4=1. 
            # Target=5 and Current=6 -> 5-6=-1.
            # Both the above are close to each other.
            # But per question we should consider the number < target. Hence we should use ABS
            if abs(target-currentSum)<howClose:
                tripletOutputSum = currentSum
                howClose=min(abs(target-currentSum),howClose)
    return tripletOutputSum

def tripletSumCloseToTarget(target,inputList):
    inputList.sort()
    smallestDistance=sys.maxsize
    outputSum=0
    for i in range(len(inputList)):
        currentNum=inputList[i]
        left=i+1
        right=len(inputList)-1
        while left<right:
            currentTripletSum=currentNum+inputList[left]+inputList[right]
            distanceFromTarget=currentTripletSum-target
            if abs(distanceFromTarget)<smallestDistance:
                smallestDistance=abs(distanceFromTarget)
                outputSum=currentTripletSum
            if currentTripletSum<target:
                left+=1
            else:
                right-=1
    return outputSum



def main():
    print(tripletSumCloseToTarget(2,[-2, 0, 1, 2]))
    print(tripletSumCloseToTarget(1,[-3, -1, 1, 2]))  
    print(tripletSumCloseToTarget(100,[1, 0, 1, 1]))

main()

"""
2 1 = 2-1=1
2 -2 = 2--2=4
-2 1=-2-1=-3
-2 2 = -2-2=-4

"""


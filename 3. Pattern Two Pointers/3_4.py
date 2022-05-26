from turtle import left


def searchTriplet(inputList):
    #If i have a sorted array i can use two pointer logic to find a pair with target sum using two pointer
    #If i am processing 3, then i would need -3(target sum) to get a 0
    inputList.sort()
    outputTriplet=[]
    for i in range(len(inputList)-1):
        currentNumber = inputList[i]
        targetSum = -currentNumber
        leftPointer = i+1
        if i>0 and inputList[i]==inputList[i+1]:
            continue
        else:
            findTriplet(inputList,targetSum,leftPointer,outputTriplet)
    return outputTriplet

def findTriplet(inputList,targetSum,leftPointer,outputTriplet):
    #Everytime i start i need the right pointer to be the last
    rightPointer=len(inputList)-1
    while leftPointer<rightPointer:
        currentSum=inputList[leftPointer]+inputList[rightPointer]
        if targetSum==currentSum:
            outputTriplet.append([-targetSum,inputList[leftPointer],inputList[rightPointer]])
            leftPointer+=1 #I am doing this because there are cases where we can find two pairs for a target sum
            rightPointer-=1 #If we dont do this then we will miss out on one pair
        elif currentSum>targetSum:
            rightPointer-=1
        else:
            leftPointer+=1
    

def main():
    print(searchTriplet([-3, 0, 1, 2, -1, 1, -2]))
    print(searchTriplet([-5, 2, -1, -2, 3]))  
main()
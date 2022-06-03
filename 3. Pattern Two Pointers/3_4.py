def searchTriplet1(inputList):
    #If i have a sorted array i can use two pointer logic to find a pair with target sum using two pointer
    #If i am processing 3, then i would need -3(target sum) to get a 0
    inputList.sort()
    outputTriplet=[]
    for i in range(len(inputList)):
        currentNumber = inputList[i]
        targetSum = -currentNumber
        leftPointer = i+1
        if i>0 and inputList[i]==inputList[i-1]:
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
            #Now that we increased LP and decreased RP, we need to figure out if the new LP and RP are different
            #We need to compare with the old P. 
            #For LP, the old will be LP-1 and for RP, the old will be RP+1
            while leftPointer<rightPointer and inputList[leftPointer]==inputList[leftPointer-1]:
                leftPointer+=1
            while leftPointer<rightPointer and inputList[rightPointer]==inputList[rightPointer+1]:
                rightPointer-=1
        elif currentSum>targetSum:
            rightPointer-=1
        else:
            leftPointer+=1

def searchTriplet(inpList):
    outputTriplets=[]
    inpList.sort()
    for i in range(len(inpList)-1):
        if inpList[i]==inpList[i+1]:
            continue
        else:
            currentNum=inpList[i]
            targetSum=-currentNum
            left=i+1
            right=len(inpList)-1
            while left<right:
                currentSum=inpList[left]+inpList[right]
                if currentSum==targetSum:
                    outputTriplets.append([currentNum,inpList[left],inpList[right]])
                    left+=1
                    right-=1
                    while inpList[left]==inpList[left-1]:
                        left+=1
                elif currentSum>=targetSum:
                    right-=1
                else:
                    left+=1
    return outputTriplets                            



def main():
    print(searchTriplet([-3, 0, 1, 2, -1, 1, -2]))
    print(searchTriplet([-5, 2, -1, -2, 3]))  
    print(searchTriplet([-1,0,1,2,-1,-4]))  
    print(searchTriplet([-2,0,0,2,2])) 
main()
def tripletsWithSmallerSum1(targetSum,inputList):
    outputList=[]
    inputList.sort()
    for i in range(len(inputList)-1):
        lP=i+1
        rP=len(inputList)-1
        numShouldBeLessThan = targetSum-inputList[i]
        # a+b+c<target
        # b+c<target-a
        # a is our current number - index i
        # b will be next index to a, so i+1
        # c will be the last index, so len(inputList)-1
        while lP<rP:
            currentSum=inputList[lP]+inputList[rP]
            if currentSum<numShouldBeLessThan:
                # if currentSum here is less than required number, then any number between them will also be less than required number
                # So we will append all those to the output list
                for j in range(rP,lP,-1):
                    outputList.append([inputList[i],inputList[lP],inputList[j]])
                lP+=1
            elif currentSum>=targetSum:
                rP-=1


    return outputList

def tripletsWithSmallerSum(targetSum,inputList):
    outputList=[]
    inputList.sort()
    for i in range(len(inputList)-1):
        currentNum=inputList[i]
        left=i+1
        right=len(inputList)-1
        while left<right:
            currentSum=currentNum+inputList[left]+inputList[right]
            if currentSum<targetSum:
                #while left<right:
                #    outputList.append([currentNum,inputList[left],inputList[right]])
                #    right-=1       Here we are decrementing RIGHT which is causing the issue. Instead we will use for loop and get all the values
                for j in range(right,left,-1):
                    outputList.append([currentNum,inputList[left],inputList[j]])
                left+=1
            elif currentSum>=targetSum:
                right-=1
    return outputList




def main():
    print(tripletsWithSmallerSum(3,[-1, 0, 2, 3]))
    print(tripletsWithSmallerSum(5,[-1, 4, 2, 1, 3]))  

main()


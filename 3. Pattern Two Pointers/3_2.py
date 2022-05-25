def removeDuplicates(inputList):
    leftPointer,rightPointer=0,1
    while rightPointer<len(inputList):
        if inputList[leftPointer]==inputList[rightPointer]:
            rightPointer+=1
        else:
            inputList[leftPointer+1],inputList[rightPointer]=inputList[rightPointer],inputList[leftPointer+1]
            leftPointer+=1
            rightPointer+=1
    return leftPointer+1

"""Let us consider first(LP 0) and second element(RP 1). If both are same, then i will just move the right pointer till i 
find the new element. After finding new element, i will have to replace left+1 with new element, then move
both left and right pointer by 1"""

def removeAllInstanceOfKeyInPlace(key,inputList):
    firstNonKeyStartsHere=0
    for i in range(len(inputList)):
        if inputList[i]==key:
            continue
        else:
            inputList[firstNonKeyStartsHere]=inputList[i]
            firstNonKeyStartsHere+=1
    return firstNonKeyStartsHere

"""First find the non key element. Till then we can keep incrementing i in for loop. After finding non key element
replace LP with that non key element. Then increment LP by 1"""
def main():
    print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
    print(removeDuplicates([2, 2, 2, 11]))  
    print(removeAllInstanceOfKeyInPlace(3,[3, 2, 3, 6, 3, 10, 9, 3]))
    print(removeAllInstanceOfKeyInPlace(2,[2, 11, 2, 2, 1]))
main()
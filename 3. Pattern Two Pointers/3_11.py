def minimumWindowSort(inpList):
    leftRequired=0
    rightRequired=0
    tempList=[]
    
    """From left lets find the first number which is smaller than previous number from left.
    Lets do the same for right. Find first number which is larger than previous number from right.
    This will give us the left and right pointer of the sub array which is not in order.
    This sublist will not be in order. We let us sort it.
    Then find the smallest and largest of the sub list.
    Now from the original list find the first element which is larger than our smallest from sublist.
    This will be final left pointer. 
    Similarly from the original list find the first element which is smaller than our largest from sublist.
    Find the length between these two. Result """

    left=0
    right=0
    while right<len(inpList):
        if right==0:
            right+=1
            continue
        leftNumber=inpList[left]
        rightNumber=inpList[right]        
        if rightNumber>=leftNumber:
            left+=1
            right+=1
        elif rightNumber<leftNumber:
            leftRequired=right
            break
    if right==len(inpList):
        return 0
    
    """Simpler While Loop Is As Follows:
    left=0
    while left<len(inpList)-1 and inpList[low]<inputList[low+1]:
        low+=1
    """

    left=len(inpList)-1
    right=len(inpList)-1
    while left>-1:
        if left==len(inpList)-1:
            left-=1
            continue
        leftNumber=inpList[left]
        rightNumber=inpList[right]        
        if leftNumber<=rightNumber:
            left-=1
            right-=1
        elif leftNumber>rightNumber:
            rightRequired=left
            break
    if left==-1:
        return 0
    
    #tempList=inpList[leftRequired,rightRequired+1]
    for i in range(leftRequired,rightRequired+1,1):
        tempList.append(inpList[i])
    tempList.sort()

    leftRequiredNumber=tempList[0]
    nextLeft=0
    while inpList[nextLeft]<leftRequiredNumber:
        nextLeft+=1
    leftRequired=nextLeft

    rightRequiredNumber=tempList[len(tempList)-1]
    nextRight=len(inpList)-1
    while inpList[nextRight]>rightRequiredNumber:
        nextRight-=1
    rightRequired=nextRight

    return rightRequired-leftRequired+1

def main():
    print(minimumWindowSort([1, 2, 5, 3, 7, 10, 9, 12])) 
    print(minimumWindowSort([1, 3, 2, 0, -1, 7, 10])) 
    print(minimumWindowSort([1, 2, 3])) 
    print(minimumWindowSort([3, 2, 1])) 
main()        
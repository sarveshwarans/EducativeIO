def findMaxTappedWater(inputBuildingHeights):
    left=0
    right=len(inputBuildingHeights)-1
    maxWaterTrapped=0
    while left<right:
        leftHeight=inputBuildingHeights[left]
        rightHeight=inputBuildingHeights[right]
        distanceBetweenBuildings=right-left
        if leftHeight<=rightHeight:
            # If there are 5 builidings between l and r, then 5*smallBuildingHeight
            # Here right building is taller. So we will use left building height
            waterTrappedHere=distanceBetweenBuildings*inputBuildingHeights[left]
            left+=1
        else:
            waterTrappedHere=distanceBetweenBuildings*inputBuildingHeights[right]
            right-=1
        maxWaterTrapped=max(maxWaterTrapped,waterTrappedHere)
    return maxWaterTrapped

"""Basically here we should not consider the buildings between buildings when we compare them.
It might sound confusing but this question is asking us to find the max water trapped between two buildings, 
IGNORING THE BUILDINGS BETWEEN THEM"""
def main():
    print(findMaxTappedWater([1,3,5,4,1])) 
    print(findMaxTappedWater([3,2,5,4,2])) 
    print(findMaxTappedWater([1,4,3,2,5,8,4])) 
main()  

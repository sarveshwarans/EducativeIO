def findMaxTappedWater(height):
    areas = 0
    max_l = max_r = 0
    l = 0
    r = len(height)-1
    while l < r:
        if height[l] < height[r]:
            if height[l] > max_l:
                max_l = height[l]
            else:
                areas += max_l - height[l]
            l +=1
        else:
            if height[r] > max_r:
                max_r = height[r]
            else:
                areas += max_r - height[r]
            r -=1
    return areas
def main():
    print(findMaxTappedWater([0,1,0,2,1,0,1,3,2,1,2,1])) 
    print(findMaxTappedWater([4,2,0,3,2,5])) 
    print(findMaxTappedWater([1,4,3,2,5,8,4])) 
main()  

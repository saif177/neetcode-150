def tappingRainWater(nums):
    n = len(nums)

    leftMax = [0] * n
    rightMax = [0] * n
    minLR = [0] * n

    res = 0

    # Build leftMax
    lmax = 0
    for i in range(n):
        leftMax[i] = lmax
        lmax = max(lmax, nums[i])

    # Build rightMax
    rmax = 0
    for i in range(n - 1, -1, -1):
        rightMax[i] = rmax
        rmax = max(rmax, nums[i])

    for i in range(n-1):
        minLR[i] = min(leftMax[i], rightMax[i])
        water = minLR[i] - nums[i]
        if water > 0 :
            res += water

    return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(tappingRainWater(height))
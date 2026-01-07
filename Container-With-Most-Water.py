def containsMostWater(nums):
    left = 0
    right = len(nums) - 1
    res = 0
    while left < right :
        base = min(nums[left], nums[right])
        temp = base * (right - left)
        res = max(res, temp)
        temp = 0
        if nums[left] <= nums[right]: left += 1
        else : right -= 1
    return res


height = [1,7,2,5,4,7,3,6]
print(containsMostWater(height))
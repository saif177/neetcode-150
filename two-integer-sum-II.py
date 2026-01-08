def twoSum2(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right :
        res = nums[left] + nums[right]
        if res == target :
            return [left+1, right]
        elif res > target:
            right -= 1
        elif res < target:
            left += 1
    return []


numbers = [1,2,3,4]
target = 3
print(twoSum2(numbers, target))
def threesum(nums):
    nums = sorted(nums)
    res = []
    for i in range(len(nums)):
        if len(nums) < 3:
            return []
        if i > 0 and nums[i] == nums[i - 1]:
            continue    
        first = nums[i]
        second = i + 1
        third = len(nums) - 1
        while second < third:
            if nums[second] + nums[third] + first > 0:
                third -= 1
            elif nums[second] + nums[third] + first < 0:
                second += 1
            else:
                res.append([nums[second], nums[third], first])
                third -= 1
                second += 1
                while nums[second] == nums[second - 1] and second < third:
                    l += 1
            
    return res
            



nums = [-1,0,1,2,-1,-4]
print(threesum(nums))
def product_except_self(nums):
    
    prefix = [0] * len(nums) 
    postfix = [0] * len(nums)
    output = [0] * len(nums)

    for i in range(len(nums)):
        if i == 0:
            prefix[i] = nums[i]
        else :
            prefix[i] = prefix[i-1] * nums[i]
    for j in range(len(nums)-1, -1, -1):
        if j == len(nums) - 1:
            postfix[j] = nums[j]
        else :
            postfix[j] = postfix[j+1] * nums[j]
    for k in range(len(nums)):
        left = 1 if k == 0 else prefix[k-1]
        right = 1 if k == len(nums) - 1 else postfix[k+1]
        output[k] = left * right
    return output

print(product_except_self([1,2,4,6]))  # Output: [24, 12, 8, 6]

def longestConsecutive( nums):
    st = set(nums)

    res = 0
    for n in nums:
        if n - 1 not in st:
            curr = n
            length = 1
            
            while curr + 1 in st:
                length += 1
                curr += 1
            res = max(length, res)
    return res

print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
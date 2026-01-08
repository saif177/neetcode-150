def isValidPalindrome(str):
    cleaned = "".join(ch for ch in s if ch.isalnum())
    left = 0
    right = len(cleaned) - 1
    while left < right:
        
        if cleaned[left].lower() != cleaned[right].lower():
            return False
        left += 1
        right -= 1
    return True
    #alternative approach
    # return cleaned == clearned[::-1]


s = "Was it a car or a cat I saw?"

print(isValidPalindrome(s))
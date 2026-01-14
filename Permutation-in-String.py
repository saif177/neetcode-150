from collections import Counter
def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False

    s1Count = Counter(s1)
    right = len(s1)
    for i in range(len(s2)):
        s2Count = Counter(s2[i: right + i])
        if s1Count == s2Count:
            return True
    return False


s1 = "trinitrophenylmethylnitramine"
s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
print(checkInclusion(s1, s2))
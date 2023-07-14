from collections import Counter

def findAnagrams(s, p):
    result = []
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])

    if s_count == p_count:
        result.append(0)

    
    for i in range(len(p), len(s)):
        s_count[s[i - len(p)]] -= 1
        if s_count[s[i - len(p)]] == 0:
            del s_count[s[i - len(p)]]

        s_count[s[i]] += 1

        if s_count == p_count:
            result.append(i - len(p) + 1)

    return result
#Driver code
s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)

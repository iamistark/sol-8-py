def minDistance(word1, word2):
    m, n = len(word1), len(word2)

    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(m - 1, -1, -1):
        dp[i][n] = dp[i + 1][n] + 1

    for j in range(n - 1, -1, -1):
        dp[m][j] = dp[m][j + 1] + 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + 1

    return dp[0][0]

# Driver code
word1 = "sea"
word2 = "eat"
result = minDistance(word1, word2)
print(result)

# 10. Regular Expression Matching
def isMatch(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[m][n] = True

    # Fill from bottom-right to top-left
    for i in range(m, -1, -1):
        for j in range(n - 1, -1, -1):
            first_match = i < m and (p[j] == s[i] or p[j] == ".")

            if j + 1 < n and p[j + 1] == "*":
                # '*' matches zero characters OR one/more of the preceding element
                dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]

    return dp[0][0]

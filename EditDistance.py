def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1)
    n = len(word2)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(n + 1):
        dp[0][i] = i 
    for i in range(m + 1):
        dp[i][0] = i
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    return dp[-1][-1]

def isSameAttr(attr1, attr2, tolerance):
    """
    :type attr1: str
    :type attr2: str
    :rtype isSame: bool
    :rtype distance: int
    """
    distance = minDistance(attr1, attr2)
    return distance <= tolerance, distance
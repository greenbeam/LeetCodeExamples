"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m):
            for j in range(-1, n):
                if j == -1:
                    if p[i] == "*":
                        dp[i+1][j+1] = dp[i-1][j+1]
                    continue
                if p[i].isalpha():
                    if p[i] == s[j]:
                        dp[i+1][j+1] = dp[i][j]
                elif p[i] == ".":
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i-1][j+1] or (dp[i+1][j] and (p[i-1] == s[j] or p[i-1] == "."))
        return dp[-1][-1]
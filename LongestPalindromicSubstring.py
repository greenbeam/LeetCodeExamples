"""
Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def check_palindrome(l, r):
            while r < len(s) and l >= 0 and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        ret = ''

        for i in range(1, len(s)):
            odd = check_palindrome(i-1, i+1)
            even = check_palindrome(i-1, i)

            temp = odd if len(odd) > len(even) else even
            ret = ret if len(ret) > len(temp) else temp

        return ret

myVar = Solution()
print(myVar.longestPalindrome('ac'))


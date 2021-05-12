"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
from itertools import cycle


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        k = 2 * numRows - 2
        sol_set = ['' for i in range(numRows)]
        idx = 0
        key = -1
        # Alternative solution

        # p_idx = [i for i in range(numRows)]
        # p2_idx = p_idx[1:-1]
        # p_idx += p2_idx[::-1]
        # for i in cycle(p_idx):
        #     sol_set[i]+=s[idx]
        #     idx+=1
        #     if idx==len(s):
        #         break

        if numRows == 1 or len(s) < numRows:
            return s
        for i in range(len(s)):
            sol_set[idx] += s[i]
            if idx == 0 or idx == numRows - 1:
                key *= -1
            idx += key

        return ''.join(sol_set)
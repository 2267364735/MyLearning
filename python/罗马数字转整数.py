"""
题目：
输入：合法罗马字符串 s，长度 1~15，字符仅含 I,V,X,L,C,D,M
输出：对应的十进制整数
规则：通常大←右，小←左；若左小右大则左值取负。
示例：s = "III" → 3；s = "IV" → 4；s = "MCMXCIV" → 1994
"""

from itertools import pairwise
ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for x, y in pairwise(s):  # 遍历相邻的罗马数字
            x, y = ROMAN[x], ROMAN[y]
            # 累加 x 的数值，y 只是用来辅助判断 x 的正负
            ans += x if x >= y else -x
        return ans + ROMAN[s[-1]]

# 最优解法
class Solution:
    SYMBOL_VALUE = {
        'I':1,
        'V':5,
        'X':10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    def romanToInt(self, s: str) -> int:
        n = len(s)
        summ = 0
        for i,p in enumerate(s):
            value = Solution.SYMBOL_VALUE[p]
            if i < n-1 and Solution.SYMBOL_VALUE[s[i+1]] > value:
                summ -= value
            else:
                summ += value
        return summ

"""
解题思路：
1. 给每个字符赋权值；从右向左扫，记录当前最大权值，遇到比最大值小（或相等）就加，比最大值大就减并更新最大值。
2. 或从左向右扫，每次看「当前」与「下一位」大小关系决定加减。
"""
"""
输入：非空字符串 s，长度 ≤ 10⁴
输出：若 s 可由其某个非空真子串重复多次构成，返回 True，否则 False
示例：
s = "abab" → True（子串 "ab" 重复 2 次）
s = "aba" → False
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]


"""
解题思路：
1. 真重复串 ⇒ 周期必然整除长度；
枚举所有可能的周期 d（1 ≤ d < n 且 n%d==0）再分段比对即可 O(n√n)。
2. 更巧办法：把 s 接在自己后面，掐头去尾，看原串还能不能在新串里找到——找到就说明有周期。
"""
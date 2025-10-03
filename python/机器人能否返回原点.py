"""
题目：
输入：字符串 moves，长度 ≤ 5000，仅含字符 'R','L','U','D'
输出：若机器人在所有移动完成后位于原点 (0,0) 返回 true，否则 false
方向无意义，每次移动一步，左右/上下分别抵消即可。
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count('U')==moves.count('D'):
            if moves.count('R')==moves.count('L'):
                return True
        return False

"""
解题思路：
1. 只关心“净位移” → 分别统计 U vs D、R vs L 的个数差。
2. 一次遍历即可同时累加四个计数器，最后看是否两方向差值均为 0。
"""
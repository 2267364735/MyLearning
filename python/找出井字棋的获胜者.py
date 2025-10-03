"""
题目：
输入：列表 moves，元素 [row, col] 表示依次落子坐标，0≤row,col≤2，先手 A 用 X，后手 B 用 O
输出：
"A" 或 "B" —— 某方已连成 3 子直线；
"Draw" —— 棋盘满且无人获胜；
"Pending" —— 仍有空位且无人获胜。
提示：可用「幻和=15」技巧或 8 条预定义直线检测。
"""

from itertools import combinations
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        SHUDU = [[6,1,8],[7,5,3],[2,9,4]]
        if 15 in [sum(k) for k in combinations([SHUDU[i][j] for i, j in moves[::2]],3)]:return "A"
        if 15 in [sum(k) for k in combinations([SHUDU[i][j] for i, j in moves[1::2]],3)]:return "B"
        return "Draw" if len(moves) == 9 else "Pending"

"""
解题思路：
1. 8 条胜利直线 → 预存行列对角线集合，或利用魔方阵「和=15」性质。
2. 分别收集 A/B 的落子集合，看是否包含任意一条胜利直线。
3. 先判胜负再判平局 / 未结束，注意顺序。
"""
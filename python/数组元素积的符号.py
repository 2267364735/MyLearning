"""
题目：
输入：整数数组 nums，长度 ≤ 1000，元素范围 [-100, 100]
输出：计算所有元素乘积的符号——正返回 1，负返回 -1，零返回 0
要求：不得使用大整数类型，尽量优化性能。
"""

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            if num == 0: return 0
            if num < 0: res *= -1
        return res


"""
解题思路：
1. 只关心符号 → 不用真乘，只数负号个数并检查 0。
2. 遇到 0 提前退出；负号个数奇偶性决定结果。
"""
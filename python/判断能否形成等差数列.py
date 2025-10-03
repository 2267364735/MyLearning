"""
题目：
输入：长度 2 ≤ n ≤ 1000 的整数数组 arr，元素范围 [-10⁶, 10⁶]
输出：若能重排使数组成等差数列，返回 true，否则 false
示例：arr = [3,5,1] → true（可排成 1,3,5）
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(1, len(arr)-1):
            if arr[i] - arr[i-1] != arr[i+1] - arr[i]:
                return False
        return True

"""
解题思路：
1. 重排后相邻差必恒定 → 先排序再扫一遍差值。
2. 只关心「公差」是否唯一，记录首两项差值后，后续逐项比对即可。
"""
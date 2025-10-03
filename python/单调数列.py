"""
题目：
输入：长度 1 ≤ n ≤ 10⁵ 的整数数组 nums
输出：若数组单调（非严格递增或非严格递减）返回 true，否则 false
注意：允许相邻元素相等。
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            if nums[i] < nums[i-1]:
                increasing = False
        return increasing or decreasing


"""
解题思路：
1. 只需知道「有没有既上升又下降」→ 用两个标志分别跟踪。
2. 一次遍历，遇到上升就关递减标志，遇到下降就关递增标志，最后看是否至少剩一个标志存活。
"""
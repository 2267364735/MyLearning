"""
输入：长度 ≤ 10⁴ 的整型列表 nums
要求：原地把所有 0 移到末尾，非零元素相对顺序不变；返回 None，直接改 nums
限制：必须在常数额外空间内完成，不得复制数组。
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1



"""
解题思路：
1. 只关心「把非零往前放」→ 用写指针记录下次放非零的位置。
2. 一次遍历：遇到非零就写到写指针处，写指针++；遍历完写指针后全填 0 即可。
3. 更紧凑写法：直接交换，省掉第二次填 0 的循环。
"""
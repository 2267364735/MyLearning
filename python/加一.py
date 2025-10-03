"""
题目：
高位到最低位排列。这个大整数不包含任何前导 0。
将大整数加 1，并返回结果的数字数组。
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str,digits))) + 1
        arr = [int(digits) for digits in str(num)]
        return arr


"""
解题思路：
1. 从最低位（数组末尾）开始模拟手算进位，carry 初始为 1。
2. 遇到 9 会变成 0 并继续向前 carry；遇到 ≤8 则直接 +1 进位结束。
3. 若循环完 carry 仍 1，则在最前面插入 1（或预分配 n+1 长度数组）。
"""
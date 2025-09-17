"""
输入：两个字符串 s、t（仅小写字母，长度 ≤ 5×10⁴）
输出：若 t 是 s 的字母异位词返回 True，否则 False
注意：字母出现次数必须完全一致，顺序可不同。
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        for ch in t:
            cnt[ord(ch) - 97] -= 1

        return all(x == 0 for x in cnt)


"""
解题思路：
1. 只关心“次数”不关心顺序 → 想到计数。
2. 字符集固定且很小（26）→ 用数组比哈希表更快。
3. 一趟加、一趟减，最后看是否全部归零。
"""
"""
题目：

"""

#方法一：暴力枚举
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+n] == needle:
                return i
        return -1


#方法二：Sunday算法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Func: 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st) - 1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st) - i
            dic["ot"] = len(st) + 1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack): return -1
        if needle == "": return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx + len(needle) <= len(haystack):

            # 待匹配字符串
            str_cut = haystack[idx:idx + len(needle)]

            # 判断是否匹配
            if str_cut == needle:
                return idx
            else:
                # 边界处理
                if idx + len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx + len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]

        return -1 if idx + len(needle) >= len(haystack) else idx

"""
解题思路：
1. 先想「如果当前窗口不匹配，主串指针能一次性跳多远」——观察窗口右侧下一个字符。
2. 给模式串每个字符预存「到串尾的距离」，缺省值取 len+1。
3. 跳转后直接从新窗口继续比对，避免回溯主串。
"""


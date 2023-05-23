'''
    给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

    字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

    说明：

    字母异位词指字母相同，但排列不同的字符串。
    不考虑答案输出的顺序。

    示例:

    输入:
    s: "cbaebabacd" p: "abc"

    输出:
    [0, 6]

    解释:
    起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
    起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need = {}
        for i in range(len(p)):
            if p[i] in need:
                need[p[i]] += 1
            elif p[i] not in need:
                need[p[i]] = 1
        have = {}
        left = -1
        right = have_size = 0
        lenth = len(s)
        need_size = len(need)
        res = []

        # 窗口内的字符都包含于need，窗口大小为[left+1, right]
        while right < lenth:
            if s[right] in need:
                if s[right] in have:
                    have[s[right]] += 1
                    # 缩小窗口，left+1为窗口左端
                    while have[s[right]] > need[s[right]]:
                        left += 1
                        if have[s[left]] == need[s[left]] or s[left] == s[right]:
                            have_size -= 1
                        have[s[left]] -= 1  
                elif s[right] not in have:
                    have[s[right]] = 1
                
                if have[s[right]] == need[s[right]]:
                    have_size += 1

            elif s[right] not in need:
                left = right
                have.clear()
                have_size = 0
            
            if have_size == need_size:
                res.append(left+1)
            
            right += 1
        return res
            

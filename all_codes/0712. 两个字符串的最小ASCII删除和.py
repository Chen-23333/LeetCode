'''
    给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。

    示例 1:

    输入: s1 = "sea", s2 = "eat"
    输出: 231
    解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
    在 "eat" 中删除 "t" 并将 116 加入总和。
    结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
    示例 2:

    输入: s1 = "delete", s2 = "leet"
    输出: 403
    解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
    将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
    结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
    如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
    注意:

    0 < s1.length, s2.length <= 1000。
    所有字符串中的字符ASCII值在[97, 122]之间。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        '''
        s1[i] == s2[j]: dp[i][j] = dp[i-1][j-1]
        s1[i] != s2[j]: dp[i][j] = min(dp[i-1][j]+ord(s1[i]),
                                       d][i][j-1]+ord(s2[j]))
        '''
        lenth1, lenth2 = len(s1), len(s2)
        dp_i_j = 0
        res = [0]
        for j in range(1, lenth2+1):
            dp_i_j += ord(s2[j-1])
            res.append(dp_i_j)
        
        for i in range(1, lenth1+1):
            pre_dp_i_j = res[0] + ord(s1[i-1])
            for j in range(1,lenth2+1):
                if s1[i-1] == s2[j-1]:
                    dp_i_j = res[j-1]
                else:
                    dp_i_j = min(res[j]+ord(s1[i-1]), pre_dp_i_j+ord(s2[j-1]))
                res[j-1] = pre_dp_i_j
                pre_dp_i_j = dp_i_j
            res[lenth2] = pre_dp_i_j
        return res[lenth2]
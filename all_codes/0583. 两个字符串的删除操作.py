'''
    给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

    示例：

    输入: "sea", "eat"
    输出: 2
    解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
     
    提示：

    给定单词的长度不超过500。
    给定单词中的字符只含有小写字母。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        '''
        word1[i] == word2[j]: dp[i][j] = dp[i-1][j-1]
        word1[i] != word2[j]: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        '''
        lenth1, lenth2 = len(word1), len(word2)
        res = [j for j in range(lenth2+1)]
        for i in range(1, lenth1+1):
            pre_dp_i_j = i
            for j in range(1,lenth2+1):
                if word1[i-1] == word2[j-1]:
                    dp_i_j = res[j-1]
                else:
                    dp_i_j = min(res[j], pre_dp_i_j) + 1
                res[j-1] = pre_dp_i_j
                pre_dp_i_j = dp_i_j
            res[lenth2] = pre_dp_i_j
        return res[lenth2]
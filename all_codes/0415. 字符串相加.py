'''
    给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

    提示：

    num1 和num2 的长度都小于 5100
    num1 和num2 都只包含数字 0-9
    num1 和num2 都不包含任何前导零
    你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/add-strings
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        res = ""
        num = 0
        while index1 >= 0 or index2 >= 0:
            if index1 >= 0:
                num += int(num1[index1])
                index1 -= 1
            if index2 >= 0:
                num += int(num2[index2])
                index2 -= 1
            res += str(num % 10)
            num = num // 10
        # 判断最高位是否还有进位
        if num > 0:
            res += str(num)
        return res[::-1]
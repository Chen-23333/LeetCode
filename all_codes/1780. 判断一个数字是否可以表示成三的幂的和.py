'''
    给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。

    对于一个整数 y ，如果存在整数 x 满足 y == 3^x ，我们称这个整数 y 是三的幂。

    

    示例 1：

    输入：n = 12
    输出：true
    解释：12 = 31 + 32
    示例 2：

    输入：n = 91
    输出：true
    解释：91 = 30 + 32 + 34
    示例 3：

    输入：n = 21
    输出：false
    

    提示：

    1 <= n <= 107

    https://leetcode.cn/problems/check-if-number-is-a-sum-of-powers-of-three/description/
'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 右侧等式按 3^x 次方不停的提取公因数，可表示为 y = 3^x1 (1 + 3^x2 (1 + 3^x3 (1 + ……)))
        while True:
            if n % 3 == 2:
                return False
            elif n % 3 == 1:
                n -= 1
            n = n / 3
            if n == 0:
                return True

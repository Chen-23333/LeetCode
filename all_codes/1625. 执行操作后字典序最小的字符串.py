'''
    给你一个字符串 s 以及两个整数 a 和 b 。其中，字符串 s 的长度为偶数，且仅由数字 0 到 9 组成。

    你可以在 s 上按任意顺序多次执行下面两个操作之一：

    累加：将  a 加到 s 中所有下标为奇数的元素上（下标从 0 开始）。数字一旦超过 9 就会变成 0，如此循环往复。例如，s = "3456" 且 a = 5，则执行此操作后 s 变成 "3951"。
    轮转：将 s 向右轮转 b 位。例如，s = "3456" 且 b = 1，则执行此操作后 s 变成 "6345"。
    请你返回在 s 上执行上述操作任意次后可以得到的 字典序最小 的字符串。

    如果两个字符串长度相同，那么字符串 a 字典序比字符串 b 小可以这样定义：在 a 和 b 出现不同的第一个位置上，字符串 a 中的字符出现在字母表中的时间早于 b 中的对应字符。例如，"0158” 字典序比 "0190" 小，因为不同的第一个位置是在第三个字符，显然 '5' 出现在 '9' 之前。

    

    示例 1：

    输入：s = "5525", a = 9, b = 2
    输出："2050"
    解释：执行操作如下：
    初态："5525"
    轮转："2555"
    累加："2454"
    累加："2353"
    轮转："5323"
    累加："5222"
    累加："5121"
    轮转："2151"
    累加："2050"​​​​​​​​​​​​
    无法获得字典序小于 "2050" 的字符串。
    示例 2：

    输入：s = "74", a = 5, b = 1
    输出："24"
    解释：执行操作如下：
    初态："74"
    轮转："47"
    累加："42"
    轮转："24"​​​​​​​​​​​​
    无法获得字典序小于 "24" 的字符串。
    示例 3：

    输入：s = "0011", a = 4, b = 2
    输出："0011"
    解释：无法获得字典序小于 "0011" 的字符串。
    示例 4：

    输入：s = "43987654", a = 7, b = 3
    输出："00553311"
    

    提示：

    2 <= s.length <= 100
    s.length 是偶数
    s 仅由数字 0 到 9 组成
    1 <= a <= 9
    1 <= b <= s.length - 1

    https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations/
'''

from math import ceil

def getCount(a: int, num: int) -> int:
    # a 的值要前置处理，只能为 1、2、5
    res = 0
    if a == 1:
        res = 10 - num
    elif a == 2:
        res = ceil((10 - num) / 2)
    elif a == 5:
        res = 1 if num >= 5 else 0
    return res


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        '''
        字典序最小，等价于 s 的具体数字的值最小。
        数字 a 只能累加至奇数位的数字上，
        可通过判断 b 的值与 s 的长度，
        计算可轮转至第 0 位、第 1 位数字的取值，并进而算出最小值。
        '''    

        if a == 3 or a == 7 or a == 9:
            # (3*7) % 10 = 1, (9*9) % 10 = 1
            a = 1
        elif a == 4 or a == 6 or a == 8:
            # (4*3) % 10 = 2, (6*2) % 10 = 2, (8*4) % 10 = 2
            a = 2

        # 寻找可被轮转至首位的具体位数
        indexList = []
        lenS = len(s)
        curIndex = lenS - b
        while True:
            if curIndex in indexList:
                break
            indexList.append(curIndex)
            curIndex = (curIndex - b) % lenS
        print("indexList = ")
        print(indexList)

        # 计算所有可轮转至首位的数字的后续数字大小
        curIndex = indexList[0]
        # 首位、次位数字累加 a 的数量
        curCount1 = getCount(a, int(s[(curIndex) % lenS]))
        curCount2 = getCount(a, int(s[(curIndex+1) % lenS]))
        if b & 1 == 0:
            curCount1 = 0
        
        for idx in indexList:
            if idx == curIndex:
                continue
            
            print("----------------------------------")
            num1 = int(s[curIndex])
            num2 = int(s[idx])
            
            # 计算当前首位取最小值时，所需要累加的 a 的次数
            count11 = curCount1
            count12 = curCount2
            count21 = getCount(a, int(s[(idx) % lenS]))
            count22 = getCount(a, int(s[(idx+1) % lenS]))

            # 如果 b 为偶数，则所有首位数字不能累加 a
            index1 = curIndex
            index2 = idx
            if b & 1 == 0:
                print("num1 = " + str(num1) + " index = " + str(curIndex))
                print("num2 = " + str(num2) + " index = " + str(idx))
                curCount1 = count11 = count21 = 0
                if num1 < num2:
                    curIndex = index1
                    curCount2 = count12
                    continue
                elif num1 > num2:
                    curIndex = index2
                    curCount2 = count22
                    continue

            # 循环比较以 num1、num2 为首的数字的大小
            compareIdx = 0
            while compareIdx < lenS:
                # 区分奇偶数进行累加
                if compareIdx & 1 == 0:
                    num1 = (int(s[(index1+compareIdx) % lenS]) + a * count11) % 10
                    num2 = (int(s[(index2+compareIdx) % lenS]) + a * count21) % 10
                else:
                    num1 = (int(s[(index1+compareIdx) % lenS]) + a * count12) % 10
                    num2 = (int(s[(index2+compareIdx) % lenS]) + a * count22) % 10
                print("num1 = " + str(num1) + " index = " + str(curIndex))
                print("num2 = " + str(num2) + " index = " + str(idx))

                if num1 == num2:
                    compareIdx += 1
                else:
                    if num1 < num2:
                        curIndex = curIndex
                        curCount1 = count11
                        curCount2 = count12
                    else:
                        curIndex = idx
                        curCount1 = count21
                        curCount2 = count22
                    break
        
        resList = list(map(int, list(s)))
        res = ""
        for i in range(lenS):
            num = resList[(curIndex + i) % lenS]
            if i & 1 == 0:
                num = (num + a * curCount1) % 10
            else:
                num = (num + a * curCount2) % 10
            res += str(num)

        return res

s = "31"
a = 4
b = 1
res = Solution().findLexSmallestString(s, a, b)
print(res)
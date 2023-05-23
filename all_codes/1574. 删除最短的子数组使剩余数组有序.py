'''
    给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

    一个子数组指的是原数组中连续的一个子序列。

    请你返回满足题目要求的最短子数组的长度。

    

    示例 1：

    输入：arr = [1,2,3,10,4,2,3,5]
    输出：3
    解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
    另一个正确的解为删除子数组 [3,10,4] 。
    示例 2：

    输入：arr = [5,4,3,2,1]
    输出：4
    解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
    示例 3：

    输入：arr = [1,2,3]
    输出：0
    解释：数组已经是非递减的了，我们不需要删除任何元素。
    示例 4：

    输入：arr = [1]
    输出：0
    

    提示：

    1 <= arr.length <= 10^5
    0 <= arr[i] <= 10^9

    https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
'''

from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 因为只能删除一个子数组，所以采用双指针的方式，确认被删除的子数组的首尾
        # arr 此时可分为 0...left, left+1...right-1, right...n-1 三部分
        n = len(arr)
        left = 0
        right = n-1

        # 先分别从首尾遍历，获取 left 和 right 的值
        while left < n-1 and arr[left] <= arr[left+1]:
            left += 1
        if left == n-1:
            # 极端场景下，无需删除
            return 0
        # right 一定大于 left，不然无需删除
        while arr[right-1] <= arr[right]:
            right -= 1

        print(arr)
        print("left = " + str(left) + ", arr[left] = " + str(arr[left]))
        print("right = " + str(right) + ", arr[right] = " + str(arr[right]))
        # left+1...right-1 明确删除，用 delMid 表示
        delMid = right - left - 1
        # 遍历 0...left，明确将左右两部分拼接时所删除元素的数量，用 delNum 表示
        # delNum = left+1 表示左侧全部删除，仅保留右侧的场景
        delNum = left + 1
        rightIndex = right
        # i 的范围为 0 <= i <= left，所以 range 取值要 left+1
        for i in range(left+1):
            # rightIndex 表示在 0...i 与 right...n-1 拼接时，
            # 右侧的拼接处的索引值，即 arr[rightIndex] >= arr[i]
            # i 递增时，rightIndex 不变或递增，且 rightIndex 最大值为 n-1
            while rightIndex < n-1 and arr[rightIndex] < arr[i]:
                rightIndex += 1
            # 左侧删除 left-i，右侧删除 rightIndex-right
            delNum = min(delNum, left-i + rightIndex-right)
        return delNum + delMid

arr = [6,3,10,11,15,20,13,3,18,12]
res = Solution().findLengthOfShortestSubarray(arr)
print(res)

# 看错了题，看成了求 arr 中删除任意元素使得 arr 非递减，求元素最少数量
class Solution2:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        length = len(arr)
        # arr 单调递减时，res 取最大值 length-1
        res = length - 1
        # resList[n] 表示从 arr[0] ~ arr[n]，在包含 n 时，所需要删除的最短子串长度
        # resList[n-m]+m 表示从 arr[0] ~ arr[n]，在不包含后 m 位时，所需要删除的子串的长度
        # res 可表示为 min{resList[n], resList[n-m]+m}(1<=m<=n)
        resList = [0]
        for i in range(1, length):
            print("-------------------------")
            print(resList)
            j = 0
            delCount = i
            while i-j > 0:
                j += 1
                if arr[i] < arr[i-j]:
                    continue
                delCount = min(delCount, resList[i-j]+j-1)
                
            resList.append(delCount)
            # arr[i] 之后还有 length-1-i 个元素
            print("delCount = " + str(delCount))
            print("delCount+length-i-1 = ", str(delCount+length-i-1))
            res = min(res, delCount+length-i-1)

        return min(res, resList[length-1])
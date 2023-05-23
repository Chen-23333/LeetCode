'''
    集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，
    导致集合丢失了一个整数并且有一个元素重复。

    给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

    示例 1:

    输入: nums = [1,2,2,4]
    输出: [2,3]
    注意:

    给定数组的长度范围是 [2, 10000]。
    给定的数组是无序的。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/set-mismatch
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        lost_num = 0
        lenth = len(nums)
        # 把对应数组内数字的索引的数字变为负数
        # 如果已经是负数，说明重复
        for i in range(lenth):
            nums_i = max(nums[i], nums[i]*(-1))
            lost_num += (i + 1 - nums_i)
            if nums[nums_i-1] > 0:
               nums[nums_i-1] *= -1
            elif nums[nums_i-1] < 0:
                res.append(nums_i)
        # lost_num 等于 丢失的数字 - 重复的数字
        res.append(lost_num + res[0])
        return res
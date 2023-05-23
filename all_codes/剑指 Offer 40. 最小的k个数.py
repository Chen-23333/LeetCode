'''
    输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

    示例 1：

    输入：arr = [3,2,1], k = 2
    输出：[1,2] 或者 [2,1]

    示例 2：

    输入：arr = [0,1,2,1], k = 1
    输出：[0]
     
    限制：

    0 <= k <= arr.length <= 10000
    0 <= arr[i] <= 10000

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 将最小的k个数，存储在大顶堆内

        # 交换堆内元素
        def exchange(res, a, b):
            temp = res[a]
            res[a] = res[b]
            res[b] = temp
        # 保持堆内元素数量不变，堆顶更新为新元素，并下沉
        def update(res, num):
            res[1] = num
            # 下沉新元素
            index = 1
            child = 2 * index
            while child <= k:
                # 判断右孩子是否存在，若存在是否大于左孩子
                if child + 1 <= k and res[child+1] > res[child]:
                    child += 1
                # child为左右孩子中的较大值
                if res[index] > res[child]:
                    break
                exchange(res, index, child)
                index = child
                child = 2 * index

        if k <= 0:
            return []
        lenth = len(arr)
        if lenth <= k:
            return arr
        res = [0]
        # 先取前k个元素构造大顶堆
        for i in range(k):
            # 插入新元素，res[0]记录当前堆内元素数量
            res.append(arr[i])
            res[0] += 1
            index = res[0]
            parent = index // 2
            
            # 上浮新元素
            while index > 1 and res[parent] < res[index]:
                exchange(res, index, parent)
                index = parent
                parent = index // 2
        for i in range(k, lenth):
            if arr[i] < res[1]:
                update(res, arr[i])
        res.pop(0)
        return res
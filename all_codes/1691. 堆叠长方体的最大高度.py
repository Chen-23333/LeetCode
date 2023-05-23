'''
    给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [widthi, lengthi, heighti]（下标从 0 开始）。请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。

    如果 widthi <= widthj 且 lengthi <= lengthj 且 heighti <= heightj ，你就可以将长方体 i 堆叠在长方体 j 上。你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。

    返回 堆叠长方体 cuboids 可以得到的 最大高度 。

    

    示例 1：



    输入：cuboids = [[50,45,20],[95,37,53],[45,23,12]]
    输出：190
    解释：
    第 1 个长方体放在底部，53x37 的一面朝下，高度为 95 。
    第 0 个长方体放在中间，45x20 的一面朝下，高度为 50 。
    第 2 个长方体放在上面，23x12 的一面朝下，高度为 45 。
    总高度是 95 + 50 + 45 = 190 。
    示例 2：

    输入：cuboids = [[38,25,45],[76,35,3]]
    输出：76
    解释：
    无法将任何长方体放在另一个上面。
    选择第 1 个长方体然后旋转它，使 35x3 的一面朝下，其高度为 76 。
    示例 3：

    输入：cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
    输出：102
    解释：
    重新排列长方体后，可以看到所有长方体的尺寸都相同。
    你可以把 11x7 的一面朝下，这样它们的高度就是 17 。
    堆叠长方体的最大高度为 6 * 17 = 102 。
    

    提示：

    n == cuboids.length
    1 <= n <= 100
    1 <= widthi, lengthi, heighti <= 100

    https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/
'''

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for e in cuboids:
            e.sort()
        # 石块堆叠要求 x1<=x2, ya<=y2, z1<=z2，所以固定以最长边为高
        cuboids.sort(key=lambda element : (element[0], element[1], element[2]), reverse=True)

        maxHeightList = [cuboids[0][2]]
        maxHeightIndex = 0

        for i in range(1, len(cuboids)) :
            curHeight = cuboids[i][2]
            
            if cuboids[i][1] <= cuboids[maxHeightIndex][1] and cuboids[i][2] <= cuboids[maxHeightIndex][2] :
                # 先判断当时石块能否直接放在当时高度最大的方案的石碓上
                curHeight += maxHeightList[maxHeightIndex]
            else :
                for j in range(i) :
                    # 遍历所有可行的方案，寻找高度最大值
                    if cuboids[i][1] <= cuboids[j][1] and cuboids[i][2] <= cuboids[j][2] :
                        curHeight = max(curHeight, cuboids[i][2] + maxHeightList[j])
            if curHeight > maxHeightList[maxHeightIndex] :
                maxHeightIndex = i
            maxHeightList.append(curHeight)
            
        return maxHeightList[maxHeightIndex]
'''
   给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。

   二叉搜索树的定义如下：

   任意节点的左子树中的键值都 小于 此节点的键值。
   任意节点的右子树中的键值都 大于 此节点的键值。
   任意节点的左子树和右子树都是二叉搜索树。


   示例 1：



   输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
   输出：20
   解释：键值为 3 的子树是和最大的二叉搜索树。
   示例 2：



   输入：root = [4,3,null,1,2]
   输出：2
   解释：键值为 2 的单节点子树是和最大的二叉搜索树。
   示例 3：

   输入：root = [-4,-2,-5]
   输出：0
   解释：所有节点键值都为负数，和最大的二叉搜索树为空。
   示例 4：

   输入：root = [2,1,3]
   输出：6
   示例 5：

   输入：root = [5,4,8,3,null,6,3]
   输出：7


   提示：

   每棵树有 1 到 40000 个节点。
   每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。

   https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/
'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTree(treeList: list) -> TreeNode:
        if len(treeList) == 0:
            return None
        nodeForCount = []
        count = 0

        while True:
            valueCount = 0
            if count == 0:
                valueCount = 1
            else:
                preNode = nodeForCount[count-1]
                for e in preNode:
                    if e != "null":
                        valueCount += 2
            count += 1

            if len(treeList) > valueCount:
                nodeValue = treeList[0:valueCount]
                del treeList[0:valueCount]
                node = []
                for value in nodeValue:
                    if value == "null":
                        node.append("null")
                    else:
                        node.append(TreeNode(val=value))
                nodeForCount.append(node)
            else:
                node = []
                for value in treeList:
                    if value == "null":
                        node.append("null")
                    else:
                        node.append(TreeNode(val=value))
                nodeForCount.append(node)
                break

        for i in range(count-1):
            nodes = nodeForCount[i]
            nextNodes = nodeForCount[i+1]
            lenNextNodes = len(nextNodes)
            subNodeIdx = 0
            for j in range(len(nodes)):
                node = nodes[j]
                if node != "null":
                    print("")
                    print("node = " + str(node.val))
                    left = nextNodes[subNodeIdx*2] if subNodeIdx*2 < lenNextNodes else "null"
                    if left != "null":
                        node.left = left
                        print("left = " + str(node.left.val))
                    right = nextNodes[subNodeIdx*2+1] if subNodeIdx*2+1 < lenNextNodes else "null"
                    if right != "null":
                        node.right = right
                        print("right = " + str(node.right.val))
                    subNodeIdx += 1
                    print("")
            print("----------")

        return nodeForCount[0][0]

def postOrderTraverse(root: TreeNode) -> tuple[Optional[int], int, Optional[int], Optional[int]]:
    if root is None:
        return None, 0, None, None
    leftSum, leftSumMax, leftMin, leftMax = postOrderTraverse(root.left)
    rightSum, rightSumMax, rightMin, rightMax = postOrderTraverse(root.right)
    maxSumValue = max(leftSumMax, rightSumMax)
    if (root.left and leftSum is None) or (root.right and rightSum is None):
        # 搜索二叉树要求该节点的左右子树都是搜索二叉树
        return None, maxSumValue, None, None

    if (leftMax and leftMax >= root.val) or (rightMin and rightMin <= root.val):
        # 搜索二叉树要求该节点的所有左子树中的值，都小于该节点，所有右子树中的值，都大于该节点
        return None, maxSumValue, None, None

    minValue = maxValue = value = root.val
    if leftSum:
        # 树的最小值，为左子树的最小值
        value += leftSum
        minValue = leftMin
    if rightSum:
         # 树的最大值，为右子树的最大值
        value += rightSum
        maxValue = rightMax
    return value, max(value, maxSumValue), minValue, maxValue
    

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        _, res, _, _ = postOrderTraverse(root)
        return res

root = [4,8,"null",6,1,9,"null",-5,4,"null","null","null",-3,"null",10]
tree = getTree(root)
res = Solution().maxSumBST(tree)
print("res = " + str(res))
'''
    给你二叉树的根节点 root 和一个整数 limit ，请你同时删除树中所有 不足节点 ，并返回最终二叉树的根节点。

    假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为 不足节点 ，需要被删除。

    叶子节点，就是没有子节点的节点。

    

    示例 1：


    输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
    输出：[1,2,3,4,"null","null",7,8,9,"null",14]
    示例 2：


    输入：root = [5,4,8,11,"null",17,4,7,1,"null","null",5,3], limit = 22
    输出：[5,4,8,11,"null",17,4,7,"null","null","null",5]
    示例 3：


    输入：root = [1,2,-3,-5,"null",4,"null"], limit = -1
    输出：[1,"null",-3,4]
    

    提示：

    树中节点数目在范围 [1, 5000] 内
    -105 <= Node.val <= 105
    -109 <= limit <= 109

    https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/
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
                    # print("")
                    # print("node = " + str(node.val))
                    left = nextNodes[subNodeIdx*2] if subNodeIdx*2 < lenNextNodes else "null"
                    if left != "null":
                        node.left = left
                        # print("left = " + str(node.left.val))
                    right = nextNodes[subNodeIdx*2+1] if subNodeIdx*2+1 < lenNextNodes else "null"
                    if right != "null":
                        node.right = right
                        # print("right = " + str(node.right.val))
                    subNodeIdx += 1
                    if (left != "null" and left.val == 499) or (right != "null" and right.val == 499):
                        print("")
                        print("node = " + str(node.val))
                        if (left != "null"):
                            print("left = " + str(node.left.val))
                        if (right != "null"):
                            print("right = " + str(node.right.val))
                        print("")
                    # print("")
            # print("----------")

        return nodeForCount[0][0]

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def modifyForLimit(root: Optional[TreeNode], limit: int, fatherSum: int) -> bool:
            if root is None:
                return False
            
            # 判断从根节点到叶子节点的链路，是否满足条件
            if root.left is None and root.right is None:
                return root.val + fatherSum >= limit
            
            leftRes = modifyForLimit(root.left, limit, fatherSum + root.val)
            rightRes = modifyForLimit(root.right, limit, fatherSum + root.val)
            
            if not leftRes:
                root.left = None
            if not rightRes:
                root.right = None

            return leftRes or rightRes
        
        res = modifyForLimit(root, limit, 0)
        return root if res else None
    
root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]
limit = 1
tree = getTree(root)
res = Solution().sufficientSubset(root=tree, limit=limit)
print(res)
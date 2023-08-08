# Kth Smallest Element in a BST (Binary Search Tree)
# Input: root = [5,3,6,2,4,null,null,1], kth = 3

# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]

        inorder_array = []
        visited_nodes_hash_set = set()

        while len(stack) > 0:
            # print(f"STACK STATUS:{stack}")
            # print(f"VISITED NODES STATUS:{visited_nodes_hash_set}")
            # print(f"\nInorder array:{[node.val for node in inorder_array]}")
            current_node = stack.pop()

            if current_node in visited_nodes_hash_set:
                inorder_array.append(current_node)
            else:
                visited_nodes_hash_set.add(current_node)
                if current_node.right is not None:
                    stack.append(current_node.right)

                stack.append(current_node)

                if current_node.left is not None:
                    stack.append(current_node.left)

        return inorder_array[k - 1].val

# -> https: // leetcode.com / problems / house - robber /
#
# Input: nums = [1, 2, 3, 1]
# 0
# 1
# 2
# 3
# Output: 4
#
# group1: 1, 3 - 4
# group2: 2, 1 - 3
#
# Input: nums = [2, 7, 9, 3, 1]
# 0
# 1
# 2
# 3
# 4
# group1: 2 + 9 + 1 = 12
# group2: 7 + 3 = 10
#
# Output: 12
#
# [1, 0, 0, 3, 0]
#
# time: O(n)
# space: O(1)
#
# [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
# [2,1,1,2]
# [1,2,3,1]
# [2,7,9,3,1]


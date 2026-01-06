# Last updated: 1/6/2026, 8:30:45 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        max_sum, ans, level = float('-inf'), 0, 0
10
11        q = collections.deque()
12        q.append(root)
13
14        while q:
15            level += 1
16            sum_at_current_level = 0
17            # Iterate over all the nodes in the current level.
18            for _ in range(len(q)):
19                node = q.popleft()
20                sum_at_current_level += node.val
21
22                if node.left:
23                    q.append(node.left)
24                if node.right:
25                    q.append(node.right)
26
27            if max_sum < sum_at_current_level:
28                max_sum, ans = sum_at_current_level, level
29           
30        return ans
31         
32            
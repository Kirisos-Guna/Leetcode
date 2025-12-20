# Last updated: 12/20/2025, 5:47:11 PM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        count = 0
4        max_count = 0
5        for num in nums:
6            if num == 1:
7                count += 1
8                max_count = max(max_count, count)
9
10            else:
11                count = 0
12
13        return  max_count
14    
15
16
17
18        
19
20
21      
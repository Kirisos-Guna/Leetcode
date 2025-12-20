# Last updated: 12/20/2025, 6:25:11 PM
1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3        count = {}
4        
5        for num in nums:
6            if num in count:
7                count[num] += 1
8            else:
9                count[num] = 1
10        duplicate = -1
11        missing = -1
12        for num in range(1, len(nums) + 1):
13            if num not in count:
14                missing = num
15            elif count[num] == 2:
16                duplicate = num
17
18        return [duplicate, missing]
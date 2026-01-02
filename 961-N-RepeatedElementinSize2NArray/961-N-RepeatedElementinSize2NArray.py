# Last updated: 1/2/2026, 9:48:52 PM
1class Solution:
2    def repeatedNTimes(self, nums: List[int]) -> int:
3        s = set() 
4        for x in nums:
5             if x in s:return x
6             s . add(x)
7
8        
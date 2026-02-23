# Last updated: 2/23/2026, 7:46:47 AM
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set() 
        for x in nums:
             if x in s:return x
             s . add(x)

        
# Last updated: 12/18/2025, 5:59:46 AM
1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        return( [val for pair in zip(nums[:n], nums[n:]) for val in pair])
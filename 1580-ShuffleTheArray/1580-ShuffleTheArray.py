# Last updated: 12/20/2025, 6:44:33 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return( [val for pair in zip(nums[:n], nums[n:]) for val in pair])
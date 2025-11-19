# Last updated: 11/19/2025, 7:54:26 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer approach
        i=1 
        for j in range (1, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        return i
        
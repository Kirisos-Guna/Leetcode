# Last updated: 11/19/2025, 7:54:29 AM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        firstindex = 0 # we use Binnary Search method
        lastindex = len(nums) - 1
        while firstindex <= lastindex:
            middleindex = (firstindex + lastindex ) // 2
            if nums [middleindex] == target:
                return middleindex
            elif nums [middleindex] > target:
                lastindex = middleindex - 1
            else:
                firstindex = middleindex + 1
        return firstindex
        
        


        
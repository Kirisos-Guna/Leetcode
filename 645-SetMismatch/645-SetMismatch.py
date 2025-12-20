# Last updated: 12/20/2025, 6:44:32 PM
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        duplicate = -1
        missing = -1
        for num in range(1, len(nums) + 1):
            if num not in count:
                missing = num
            elif count[num] == 2:
                duplicate = num

        return [duplicate, missing]
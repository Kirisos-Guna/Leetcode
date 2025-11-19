# Last updated: 11/19/2025, 7:54:25 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Two-Pass Hash Table
        numMap={}
        n=len(nums)

        #Build the hash table
        for i in range(n):
            numMap[nums[i]]=i

        #Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] !=i:
                return [i, numMap[complement]]
        
        return
        
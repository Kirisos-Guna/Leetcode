# Last updated: 2/23/2026, 7:46:49 AM
class Solution:
    def addDigits(self, num: int) -> int:
         while num>9:
            num = num%10 + num//10
         return num
            
    
 
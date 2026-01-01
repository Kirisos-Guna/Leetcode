# Last updated: 1/1/2026, 3:06:28 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3
4        n = len(digits)
5        for i in range(n-1, -1 , -1):
6            if digits[i] < 9:
7                digits[i] += 1
8                return digits 
9            digits[i] = 0
10        return[1]+digits
11            
12
13
14      
# Last updated: 12/1/2025, 6:57:30 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        for i in range(len(digits) -1, -1, -1):
4            if digits[i] == 9:
5                digits[i] = 0
6            else:
7                digits[i] = digits[i] + 1
8                return digits
9        return [1] + digits
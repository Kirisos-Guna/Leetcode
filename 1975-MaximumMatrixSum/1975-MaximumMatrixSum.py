# Last updated: 1/5/2026, 9:01:14 PM
1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        total_sum = 0
4        min_abs_val = float("inf")
5        negative_count = 0
6
7        for row in matrix:
8            for val in row:
9                total_sum += abs(val)
10                if val < 0:
11                    negative_count += 1
12                min_abs_val = min(min_abs_val, abs(val))
13
14        # Adjust if the count of negative numbers is odd
15        if negative_count % 2 != 0:
16            total_sum -= 2 * min_abs_val
17
18        return total_sum
19        
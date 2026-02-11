# Last updated: 2/11/2026, 6:44:59 AM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        midx = m - 1
4        nidx = n - 1 
5        right = m + n - 1
6
7        while nidx >= 0:
8            if midx >= 0 and nums1[midx] > nums2[nidx]:
9                nums1[right] = nums1[midx]
10                midx -= 1
11            else:
12                nums1[right] = nums2[nidx]
13                nidx -= 1
14
15            right -= 1
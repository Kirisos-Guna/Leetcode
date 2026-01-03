# Last updated: 1/3/2026, 8:39:36 PM
1class Solution:
2    def numOfWays(self, n: int) -> int:
3        MOD = 10**9 + 7
4
5        same, diff = 6,6
6
7        for i in range(n-1):
8            new_same = (3 * same + 2 * diff) % MOD
9            new_diff = (2 * same + 2 * diff) % MOD
10            same, diff = new_same, new_diff
11
12        return (same + diff) % MOD
13        
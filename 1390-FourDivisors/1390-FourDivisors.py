# Last updated: 1/4/2026, 8:32:20 PM
1class Solution:
2    def sumFourDivisors(self, nums: List[int]) -> int:
3        res = 0
4        for n in nums:
5            val = self.sumOne(n)
6            if val != -1:
7                res += val
8        return res
9
10    def sumOne(self, n: int) -> int:
11        p = round(n ** (1/3))
12        if p ** 3 == n and self.isPrime(p):
13            return 1 + p + p*p + p*p*p
14
15        for i in range(2, int(n ** 0.5) + 1):
16            if n % i == 0:
17                a, b = i, n // i
18                if a != b and self.isPrime(a) and self.isPrime(b):
19                    return 1 + a + b + n
20                return -1
21        return -1
22
23    def isPrime(self, x: int) -> bool:
24        if x < 2:
25            return False
26        for i in range(2, int(x ** 0.5) + 1):
27            if x % i == 0:
28                return False
29        return True
30        
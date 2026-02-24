# Last updated: 2/24/2026, 6:46:21 AM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
        
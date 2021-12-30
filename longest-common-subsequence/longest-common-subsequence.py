import collections
import bisect
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        d = collections.defaultdict(list)
        for i, c in enumerate(text2):
            d[c].append(i)
        print(d)
        for c in text1:
            if c in d:
                for i in reversed(d[c]):
                    ins = bisect.bisect_left(dp, i)
                    if ins == len(dp):
                        dp.append(i)
                    else:
                        dp[ins] = i
        return len(dp)
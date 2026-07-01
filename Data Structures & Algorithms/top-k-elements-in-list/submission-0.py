from collections import defaultdict as dd
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = dd(int)
        for n in nums:
            cnt[n] += 1
        ans = []
        lcnt = list(sorted(cnt.items(), key=lambda x:x[1]))
        return [num for num, count in lcnt[-k:]]
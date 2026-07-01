from collections import defaultdict as dd
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        di = dd(bool)
        for n in nums:
            if di[n] == False:
                di[n] = True
            else:
                return True
        return False
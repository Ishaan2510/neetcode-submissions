from collections import defaultdict as dd
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ds = dd(list)
        for word in strs:
            key = "".join(sorted(word))
            ds[key].append(word)
        return list(ds.values())





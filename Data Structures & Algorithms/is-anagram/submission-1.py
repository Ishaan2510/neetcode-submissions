from collections import defaultdict as dd
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = dd(int)
        d_t = dd(int)
        for i in s:
            if i not in d_s.keys():
                d_s[i] = 1
            else:
                d_s[i] += 1
        for i in t:
            if i not in d_t.keys():
                d_t[i] = 1
            else:
                d_t[i] += 1
        for c, cnt in d_s.items():
            if c not in d_t.keys() or cnt != d_t[c]:
                return False
        for c, cnt in d_t.items():
            if c not in d_s.keys() or cnt != d_s[c]:
                return False
        return True



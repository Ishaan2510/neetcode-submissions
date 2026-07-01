from collections import defaultdict as dd
class Solution:
    def encode(self, strs: List[str]) -> str:
        output_enc = []
        for st in strs:
            l = len(st)
            encoded = str(l) + "@" + st
            output_enc.append(encoded)
        return "".join(output_enc)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "@":
                j += 1

            length = int(s[i:j])

            word = s[j+1:j+1+length]

            res.append(word)

            i = j + 1 + length

        return res
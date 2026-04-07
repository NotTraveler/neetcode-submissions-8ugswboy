import codecs
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for st in strs:
            st = f"{st}<<[1221212]"
            encoded += st
        return encoded

    def decode(self, s: str) -> List[str]:
        new_sts = []
        start = 0
        for i,letter in enumerate(s):
            if letter == "<":
                end = i
                if s[i:i+11] == "<<[1221212]":
                    new_sts.append(s[start:i])
                    start = i+11 
        return new_sts
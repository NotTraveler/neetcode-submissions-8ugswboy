from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for itm in strs:
            sorteditm = "".join(sorted(itm))
            anagram[sorteditm].append(itm)
        lst = [i for i in anagram.values()]
        return lst
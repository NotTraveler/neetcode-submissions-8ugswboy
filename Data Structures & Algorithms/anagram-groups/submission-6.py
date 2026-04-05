from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        itm = defaultdict(list)
        for st in strs:
            new_str = "".join(sorted(st))
            itm[new_str].append(st)
        lst = [i for i in itm.values()]
        return lst
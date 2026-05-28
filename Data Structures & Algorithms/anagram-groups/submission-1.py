from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)
        
        for i in range(len(strs)):

            anagram_type = ''.join(sorted(strs[i]))


            d[anagram_type].append(i)

        res = []

        for anagram_type, idx_lst in d.items():
            res.append([strs[idx] for idx in idx_lst])

        return res
            
        
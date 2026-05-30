class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ''

        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        
        return res



    def decode(self, s: str) -> List[str]:

        res = []

        i = 0

        while i < len(s):
            
            cur_len = ''

            while s[i] != '#':
                cur_len += s[i]
                i += 1
            
            cur_len = int(cur_len)

            cur_s = s[i + 1: i + 1 + cur_len]

            res.append(cur_s)

            i += 1 + cur_len

        
        return res

        






